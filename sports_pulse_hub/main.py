
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import neca
from neca.events import *
from neca.generators import generate_data
import time
from flask import Flask, request
import neca.log
from neca.settings import app, socket
import external_function


generate_data("sports-20191117.txt", time_scale=10000)

last_tweet_time = 0
tweet_interval = 0.5
tweets = []

positive_tweets_count=0
negative_tweets_count=0

tweets_sixtienth=0
tweets_seventienth=0

@event("init")
def init(ctx, data):
    global last_tweet_time
    last_tweet_time = time.time()
    print("init")

@event("tweet")
def tweet(ctx, data):
    global last_tweet_time, positive_tweets_count, negative_tweets_count,tweets_sixtienth,tweets_seventienth
    current_time = time.time()
    if current_time - last_tweet_time >= tweet_interval:
        print("tweeted")
        tweets.append(data)
        emit("x", data)
        emit("tweets", data)
        emit("add_top_accounts",external_function.sort_by_followers(tweets))
        top_tweets=external_function.sort_by_retweet_count(tweets)
        emit("add_top_tweets",top_tweets)
        sentiment_analysis=external_function.get_sentiment_analysis(data,positive_tweets_count,negative_tweets_count)
        positive_tweets_count=sentiment_analysis[0]
        negative_tweets_count=sentiment_analysis[1]
        neutral_tweets_count=len(tweets)-positive_tweets_count-negative_tweets_count
        emit("sentiment_analysis",{"positive_tweets":positive_tweets_count,"negative_tweets":negative_tweets_count,"neutral_tweets":neutral_tweets_count})
        activity= external_function.get_tweet_activity(data,sixtienth=tweets_sixtienth,seventieth=tweets_seventienth)
        tweets_sixtienth=activity[0]
        tweets_seventienth=activity[1]
        emit("tweets_activity",{"sixtienth":activity[0],"seventieth":activity[1]})
        last_tweet_time = current_time

# @app.route('/chart') def chart_html(): return reder_template('charts.html') if_name__ == '__main__': socketio.run(app, debug = True)

@app.route('/search', methods=['POST'])
def search():
    response=request.json
    words=response.split(' ')
    matching_tweets=[]
    for word in words:
        matching_tweets.extend(external_function.search_by_value(data_dict=tweets,search_value=word))
        if(len(matching_tweets)==20):
            break
    
    emit('search',matching_tweets)


    return 'hello world', 200 # returns 'hello world' with a status code of 200 (OK)



# starts the server and prevents the program from exiting
neca.start()                 