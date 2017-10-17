'''
Code adapted from http://pythonforengineers.com/build-a-reddit-bot-part-1/
-Script that returns all posts with over 300 points within a given day
Modified by Joseph Yeung
'''

import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('buildapcsales') #Change this to any subreddit

for submission in subreddit.top(time_filter='day'):
    if submission.score >= 300:
        print('Title: ', submission.title)
        print('Score: ', submission.score)
        print('Link: ', submission.shortlink)
        print('----------------------------------\n')
