'''
Code adpated from http://pythonforengineers.com/build-marvin-the-depressed-reddit-bot-in-python/
Original json joke file from https://raw.githubusercontent.com/taivop/joke-dataset/master/stupidstuff.json


-Reddit bot that replies to comments with a random joke when prompted with 'tell me a joke'
Modified by Joseph Yeung
'''

import praw
import random
import re
import json

MIN_RATING = 3.0
MAX_JOKE_LENGTH = 200

reddit = praw.Reddit('bot1')

#Open json file containing jokes
with open('jokes_json.txt', 'r') as f:
    joke_list = json.loads(f.read())    
    
subreddit = reddit.subreddit('pythonforengineers')

#Continually monitor new comments in a subreddit for keyphrase
for comment in subreddit.stream.comments():
    if re.search('tell me a joke', comment.body, re.IGNORECASE):
        print('Found someone in need a joke!')
        
        #Find a random & valid joke within jokelist
        joke_found = False
        while not joke_found:
            try:
                joke_dict = random.choice(joke_list)
                joke = joke_dict['body']
                joke_found = True if joke != '' and len(joke) < MAX_JOKE_LENGTH \
                    and joke_dict['rating'] >= MIN_RATING else False
            except UnicodeEncodeError:
                pass
        
        jokebot_reply = 'clown_bot has a joke for you:\n' + joke
        comment.reply(jokebot_reply)
        print(jokebot_reply)
