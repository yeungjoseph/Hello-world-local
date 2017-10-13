import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []
else:
    with open('posts_replied_to.txt', 'r') as f:
        posts_replied_to = list(filter(None,f.readlines())) #filter out empty elements of list

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search('i love python', submission.title, re.IGNORECASE):
            submission.reply('Botty bot says: Me too!!')
            print('Bot replying to : ', submission.title)
            posts_replied_to.append(submission.id)
            
with open('posts_replied_to.txt', 'w') as f:
    for post_id in posts_replied_to:
        f.write(post_id + '\n')