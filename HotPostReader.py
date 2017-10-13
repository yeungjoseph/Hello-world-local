#Tutorial taken from http://pythonforengineers.com/build-a-reddit-bot-part-1/

import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('pythonforengineers')

for submission in subreddit.hot(limit=5):
    print('Title: ', submission.title)
    print('Text: ', submission.selftext)
    print('Score: ', submission.score)
    print('----------------------------------\n')
