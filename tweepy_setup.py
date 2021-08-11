import tweepy
from tweepy import StreamListener
from dotenv import load_dotenv
from os import environ as env
from kafka import KafkaProducer
import json
from pprint import pprint
from datetime import datetime

load_dotenv()
TOPIC = env.get("KAFKA_TOPIC")

## Helper functions to get stream details. Make sure .env is setup with API keys
def __get_twitter_auth() -> tweepy.OAuthHandler:
    auth = tweepy.OAuthHandler(
        consumer_key=env.get("CONSUMER_KEY", ""),
        consumer_secret=env.get("CONSUMER_SECRET", "")
    )

    auth.set_access_token(
        env.get("ACCESS_TOKEN", ""),
        env.get("ACCESS_TOKEN_SECRET", "")
    )
    return auth

def get_twitter_api() -> tweepy.API:
    auth = __get_twitter_auth()
    return tweepy.API(auth)


class StdOutListener(StreamListener):
    def __init__(self, producer: KafkaProducer, api=None):
        super().__init__(api=api)
        self.producer = producer


    def on_data(self, raw_data):
        data = json.loads(raw_data.encode('utf8', 'replace'))
        data['test_dat'] = '5'
        tweet_date = datetime.strptime(data["created_at"], "%a %b %d %H:%M:%S %z %Y")
        #print(tweet_date)
        data["created_at"] = tweet_date.strftime("%Y-%m-%d %H:%M:%S")
        #pprint(data)

        
        #pprint(data)
        #print("data")
        pprint(data)
        #valid = super.on_datra
        #if valid := super().on_data(raw_data):
        #print(raw_data)
        #print("*"*50)
        #print(raw_data)
        #print(data)
        self.producer.send(TOPIC, data)
        return True
    
    def on_error(self, status_code):
        print(status_code)

def get_twitter_stream(producer, listener=None) -> tweepy.Stream:
    listener = listener if listener is not None else StdOutListener(producer)
    auth = __get_twitter_auth()

    return tweepy.Stream(auth, listener=listener)



