import external_function
from neca.events import event
from main import tweets
from neca.settings import app, socket
from external_function import search_by_location,get_retweet,get_followers,search_by_value,sort_by_country,sort_by_followers,sort_by_retweet_count

@app.route('/search')
def search_handler(context,data):
    return search_by_value(search_value=data,data_dict=tweets)

@event('search_location_event')
def search_location_handler(context,data):
    return search_by_location(data_dict=tweets,location=data)

@event('sort_by_followers_event')
def sort_by_followers_handler(context,data):
    return sort_by_followers(data_dict=tweets)    

@app.route('sort_by_country_event')
def sort_by_country_handler(context,data):
    return sort_by_country(data_dict=tweets)

@app.route('sort_by_retweet_count')
def sort_by_retweet_count_handler(context,data):
    return sort_by_retweet_count(data_dict=tweets)


@app.route('sort_by_retweet_count')
def sort_by_retweet_count_handler(context,data):
    return sort_by_retweet_count(data_dict=tweets)


@event('search_football')
def search_football_handler(context,data):
    return search_by_value(search_value='football',data_dict=tweets)

@event('search_basketball')
def search_football_handler(context,data):
    return search_by_value(search_value='basketball',data_dict=tweets)

@event('search_volleyball')
def search_football_handler(context,data):
    return search_by_value(search_value="volleyball",data_dict=tweets)

@event('search_netherlands')
def search_netherlands_handler(context,data):
    return search_by_location(search_value='netherlands',data_dict=tweets)

@event('search_germany')
def search_germany_handler(context,data):
    return search_by_value(search_value='germany',data_dict=tweets)
