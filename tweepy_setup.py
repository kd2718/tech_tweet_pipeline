import tweepy
from dotenv import load_dotenv
from os import environ as env
from pprint import pprint

load_dotenv()

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

def get_twitter_stream():
    pass



