import tweepy
from tweepy import StreamListener
from dotenv import load_dotenv
from os import environ as env
from kafka import KafkaProducer

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
        #print("data")
        #valid = super.on_datra
        #if valid := super().on_data(raw_data):
        #print(raw_data)
        #print("*"*50)
        self.producer.send(TOPIC, raw_data)
        return True
    
    def on_error(self, status_code):
        print(status_code)

def get_twitter_stream(producer, listener=None) -> tweepy.Stream:
    listener = listener if listener is not None else StdOutListener(producer)
    auth = __get_twitter_auth()

    return tweepy.Stream(auth, listener=listener)



