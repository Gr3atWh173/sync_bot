import praw
import facebook
from config import *
from time import sleep

def get_posts(api, n):
    return api.subreddit(SUBREDDIT).new(limit=n)

def post_to_facebook(api, post):
    author = post.author
    body = None
    if post.is_self:
        body = post.selftext
    else:
        body = post.url
    original = "https://www.reddit.com/" + str(post.id)
    title = post.title
    msg = "Title: {}\n\nOriginal Poster: {}\nOriginal Post: {}\n\nBody:\n{}".format(title, author, original, body)
    try:
        api.put_wall_post(msg)
    except facebook.GraphAPIError:
        pass

#get the reddit api
reddit_api = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                         client_secret=REDDIT_APP_SECRET,
                         user_agent=REDDIT_USER_AGENT)

#get the facebook api
facebook_api = facebook.GraphAPI(FACEBOOK_PAGE_ACCESS_TOKEN)

running = True
while running:
    #pull down posts from reddit
    posts = get_posts(reddit_api, 10)
    #post them to facebook
    for post in posts:
        post_to_facebook(facebook_api, post)
    sleep(10)
