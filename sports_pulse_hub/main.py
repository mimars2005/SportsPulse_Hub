import neca
from neca.events import *
from neca.generators import generate_data
import time

generate_data("sports-20191117.txt", time_scale=1000)

# your code here
last_tweet_time = 0
tweet_interval = 6

@event("init")
def init(ctx, data):
    global last_tweet_time
    last_tweet_time = time.time()
    print("init")

@event("tweet")
def tweet(ctx, data):
    global last_tweet_time
    current_time = time.time()
    if current_time - last_tweet_time >= tweet_interval:
        print("tweeted")
        emit("x", data)

        last_tweet_time = current_time

# starts the server and prevents the program from exiting
neca.start()                 