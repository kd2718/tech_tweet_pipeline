from kafka import KafkaProducer
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

def get_kafka_producer():
    prod = KafkaProducer(bootstrap_servers=env.get("KAFKA_SERVER", "localhost:9092"))
    return prod


if __name__ == "__main__":
    prod = get_kafka_producer()
    print(prod)
    for i in range(100):
        prod.send("foobar", bytes(f"here are my bytes {i}", "utf8" ))

    print("finished")