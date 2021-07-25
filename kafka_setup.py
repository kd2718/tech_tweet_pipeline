from kafka import KafkaProducer
from dotenv import load_dotenv
from os import environ as env
from main import get_auth

load_dotenv()

def get_kafka_producer():
    prod = KafkaProducer(bootstrap_servers=env.get("KAFKA_SERVER", "localhost:9092"))
    return prod


if __name__ == "__main__":
    auth = get_auth()
    prod = get_kafka_producer()
    print(prod)
    for i in range(100):
        prod.send("foobar", bytes(f"here are my bytes {i}", "utf8" ))

    print("finished")