from kafka import KafkaProducer, KafkaConsumer
from dotenv import load_dotenv
from os import environ as env
import json

load_dotenv()
TOPIC = env.get("KAFKA_TOPIC")

def get_kafka_producer():
    prod = KafkaProducer(
        bootstrap_servers=env.get("KAFKA_SERVER", "localhost:9092"),
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return prod

def get_kafka_consumer(topic=TOPIC):
    print(f"topic set to {topic}")
    consumer = KafkaConsumer(topic, bootstrap_servers=env.get("KAFKA_SERVER", "localhost:9092"))
    return consumer


if __name__ == "__main__":
    #auth = get_auth()
    prod = get_kafka_producer()
    print(prod)
    for i in range(100):
        prod.send("foobar", bytes(f"here are my bytes {i}", "utf8" ))
    prod.flush()

    print("finished")