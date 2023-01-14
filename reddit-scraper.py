import praw
from dotenv import load_dotenv
load_dotenv()
import os
reddit = praw.Reddit(client_id=os.environ.get('CLIENT_ID'), client_secret=os.environ.get('CLIENT_SECRET'), user_agent=os.environ.get('USER_AGENT'))
# get 10 hot posts from the rutgers subreddit
hot_posts = reddit.subreddit('rutgers').hot(limit=10)
for post in hot_posts:
    print(post.title)
    
# get 10 hot posts from the MachineLearning subreddit
hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)
for post in hot_posts:
    print(post.title)


# get hottest posts from all subreddits
hot_posts = reddit.subreddit('all').hot(limit=10)
for post in hot_posts:
    print(post.title)
    
import pandas as pd
posts = []
ml_subreddit = reddit.subreddit('rutgers')
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)

ml_subreddit = reddit.subreddit('rutgers')

print(ml_subreddit.description)

submission = reddit.submission(url="https://www.reddit.com/r/MapPorn/comments/a3p0uq/an_image_of_gps_tracking_of_multiple_wolves_in/")
from praw.models import MoreComments
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)

submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)
    
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    print(comment.body)

