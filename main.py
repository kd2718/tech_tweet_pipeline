import tweepy
from dotenv import load_dotenv
from os import environ as env
from pprint import pprint
from tweepy_setup import get_twitter_api

load_dotenv()

# this is a demo to make sure everyting is working

if __name__ == "__main__":

    api = get_twitter_api()

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
        print("*"*30)