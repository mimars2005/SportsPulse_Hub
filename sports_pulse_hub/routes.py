from events import search_handler
from flask import request
import external_function 
from neca.settings import app
from main import tweets
from neca.events import emit,fire_global
import main
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

#@app.route('/search_emotion', methods = ['POST'])
#def search_by_emotion():
    

@app.route('/sort_followers', methods=['POST'])
def sort_by_followers(data_dict):
    emit('sort_by_followers_event',external_function.sort_by_followers(data_dict=tweets))

@app.route('/sort_by_retweets', methods = ['POST'])
def sort_by_retweet_count(data_dict):
    sorted_list=sorted(data_dict,key=lambda a:external_function.get_retweet(a),reverse=True) 
    return sorted_list
@app.route('/sort_by_country', methods = ['POST'])
def sort_by_country(data_dict):
    sorted_list=sorted(data_dict,key=lambda a:external_function.get_retweet(a),reverse=True) # sort by retweets count, decreasingly
    return sorted_list
