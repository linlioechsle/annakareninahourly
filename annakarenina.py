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

 
#handles big sentences
prev_sentence = 'last_sentence.txt'
def split_long(string, length):
  return (string[0+i:length+i] for i in range(0, len(string), length))

#open book file
f = open("updatedannak.txt", "r")
string_no_breaks = ""

for line in f:
  line.replace('_', '')
  stripped_line = line.rstrip()
  string_no_breaks += stripped_line
  string_no_breaks += " "

f.close()

#tokenizes book list of strings
from nltk.tokenize import sent_tokenize, word_tokenize
list = sent_tokenize(string_no_breaks)

#tweets!
for sentence in list:
  for chunk in split_long(sentence, 280):
    api.update_status(chunk)
    time.sleep(1770)


