import praw  # noqa pylint: disable=all 


reddit = praw.Reddit(
     client_id="IbE0_q5MkfFYug",
     client_secret="C5K8QD24PcC3UwXdOT7Qx2F1LZiZWg",
     user_agent="testapi"
 )

subreddit = reddit.subreddit("linuxmemes")
print(subreddit.url)


def gifs(val="gifs"):
    sub = reddit.subreddit(val).random()
    return sub.title, sub.selftext, sub.url


def memes(val="linuxmemes"):
    sub = reddit.subreddit(val).random()
    return sub.title, sub.selftext, sub.url
