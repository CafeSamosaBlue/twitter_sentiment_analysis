import tweepy
from textblob import TextBlob
import csv
import io

THRESHOLD = 0.5

# Step 1 - Authenticate
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'

access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 3 - Retrieve Tweets
public_tweets = api.search('anime')

# CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
# and label each one as either 'positive' or 'negative', depending on the sentiment
# You can decide the sentiment polarity threshold yourself
dataset = [['Tweet', 'Sentiment']]

for tweet in public_tweets:
    text = tweet.text
    polarity = TextBlob(tweet.text).sentiment.polarity
    sentiment = 'positive' if polarity >= THRESHOLD else 'negative'
    dataset.append([text, sentiment])

with io.open("tweets.csv", 'w', encoding="utf-8", newline='') as tweets:
    writer = csv.writer(tweets)
    writer.writerows(dataset)
