import os
import tweepy

def check_latest_tweet():
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)
    user_id = "44196397"  # Elon Musk's user ID
    tweets = client.get_users_tweets(user_id, max_results=5)
    
    if tweets and tweets.data:
        latest = tweets.data[0].text
        print("Latest Tweet:", latest)
    else:
        print("No tweets found.")

if __name__ == "__main__":
    check_latest_tweet()
