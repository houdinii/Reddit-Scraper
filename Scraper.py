# Scraper.py - A program that monitors a user's choice of subreddit and downloads a specified number of images from
# /hot every day.

import praw
import urllib, requests
import os, re, sys

user_sub = sys.argv[1]
print(user_sub)

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit(user_sub)
query = ' '.join(sys.argv[2:])

def main():
    if not os.path.isdir('Downloaded/' + query):
        os.mkdir('Downloaded/' + query)

    os.chdir('Downloaded/' + query)

    for submission in subreddit.hot():
        if query in submission.title:
            print(str(submission.score) + ' - ' + submission.title)
            print(submission.domain)
            fetch_data(submission)

def fetch_data(submission):
    #TODO: Add GIF support
    if submission.domain == 'gfycat.com':
        return
    elif submission.domain == 'imgur.com':
        # Unfortunately Imgur broke the function on their website which allows a user to download
        # an album as a zip so albums are not currently supported by this program.
        #urllib.request.urlretrieve(submission.url + '/zip', submission.title.rstrip() + '.zip')
        return
    else:
        urllib.request.urlretrieve(submission.url, submission.title.rstrip() + '.png')

#if not os.path.isfile('viewed_posts.txt'):
#    viewed_posts = []
#else:
#    with open('viewed_posts.txt', 'r') as file:
#        viewed_posts = file.read()
#        viewed_posts = viewed_posts.split('\n')
#        viewed_posts = list(filter(None, viewed_posts))

#for submission in subreddit.hot(limit=5):
#    if submission.id not in viewed_posts:
#        print('Title: ' + submission.title)
#        print(submission.score)
#        viewed_posts.append(submission.id)

#with open('viewed_posts.txt', 'w') as file:
#    for post_id in viewed_posts:
#        file.write(post_id + '\n')

if __name__ == '__main__':
    main()