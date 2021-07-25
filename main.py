import tweepy
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

# this is a demo to make sure everyting is working

def get_auth():
    auth = tweepy.OAuthHandler(
        consumer_key=env.get("CONSUMER_KEY", ""),
        consumer_secret=env.get("CONSUMER_SECRET", "")
    )

    auth.set_access_token(
        env.get("ACCESS_TOKEN", ""),
        env.get("ACCESS_TOKEN_SECRET", "")
    )
    return auth



if __name__ == "__main__":

    auth = get_auth()
    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
        print("*"*30)