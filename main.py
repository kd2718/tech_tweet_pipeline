import tweepy
from dotenv import load_dotenv
from os import environ as env
from pprint import pprint
from tweepy_setup import get_twitter_api, get_twitter_stream
from kafka_setup import get_kafka_consumer, get_kafka_producer
from kafka import KafkaConsumer
import json
import time
from pprint import pprint

load_dotenv()

# this is a demo to make sure everyting is working
DEBUG = False

if __name__ == "__main__":

    api = get_twitter_api()
    producer = get_kafka_producer()
    stream = get_twitter_stream(producer)
    #stream.filter(track=["python", ])
    print("start stream")
    stream.filter(
        track=["#python", "#kotlin", "#c#", "#dotnet", "#rust", "#java", "#f#", "#c++", "#javascript"], 
        is_async=True
    )

    while True:
        producer.flush()
        time.sleep(5)
        if DEBUG is True:
            break

    consumer = get_kafka_consumer()

    for msg in consumer:
        print(type(msg))
        pprint(json.loads(msg.value))
        #print(json.loads(msg))
        #jmsg = json.loads(msg.value)
        #print(jmsg)
        break


