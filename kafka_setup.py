from kafka import KafkaProducer
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

prod = KafkaProducer(bootstrap_servers=env.get("KAFKA_SERVER", "localhost:9092"))