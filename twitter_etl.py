import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():

    # API credentials
    consumer_key = "o6gC6rXjXxR9vbdPmSHfHE240"
    consumer_secret = "VHJMJqhPRHL6XdwqDEKkna2DZaGOaXrYyq16dHrAsX4zsAWREc"
    access_token = "1894101610701209600-1SEh0aSlT6GAHabyfQg0P9AGo63pMq"
    access_token_secret = "nOioQObZkvFBbMTqjiLwh7AKJwl2a80YDPeBGeAhNYATe"

    # Correct authentication setup
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # API object creation
    api = tweepy.API(auth)

    # Fetch tweets
    tweets = api.user_timeline(screen_name='@elonmusk',
                                count=200,
                                include_rts=False,
                                tweet_mode='extended')
        

    tweet_list =[]
    for tweet in tweets:
        text = tweet._json["full_text"]

        # dict
        refined_tweet = {"user": tweet.user.screen_name, 
                        "text": text,
                        "fav_count": tweet.favorite_count, 
                        "retweet_count": tweet.retweet_count,
                        "created_at": tweet.created_at}
        
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv("elonMuskTwitterData.csv")

    '''
    To Add it to S3 bucket:
        df.to_csv("s3://bucket_name/filename.csv")
    '''


