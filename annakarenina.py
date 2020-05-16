import tweepy
import time
import os

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#source: https://www.reddit.com/r/learnpython/comments/3xuych/least_resource_intensive_way_to_delete_first_line/cy7zm17?utm_source=share&utm_medium=web2x
def deleteFirstLine():
  with open('updatedannak.txt', 'r+') as f:
    f.readline()
    data = f.read()
    f.seek(0)
    f.write(data)
    f.truncate()

book = open("updatedannak.txt", "r+")

for line in book:
  if line != "\n":
    api.update_status(line)
    print("Tweeting and removing from file: " + line)
    deleteFirstLine()
    time.sleep(1740)
    
book.close()
