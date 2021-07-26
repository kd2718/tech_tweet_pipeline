import tweepy
from dotenv import load_dotenv
from os import environ as env
from pprint import pprint
from tweepy_setup import get_twitter_api, get_twitter_stream
from kafka_setup import get_kafka_producer

load_dotenv()

# this is a demo to make sure everyting is working

if __name__ == "__main__":

    api = get_twitter_api()
    producer = get_kafka_producer()
    stream = get_twitter_stream(producer)
    stream.filter(track=["covid", ])
