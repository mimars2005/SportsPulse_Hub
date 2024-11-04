# search function
# top tweets
# latest tweets
# tweet aggregation

import json
# Search Functions

positive_words = {"good", "happy", "love", "great", "excellent", "amazing", "positive", "awesome", "nice", "fantastic"}
negative_words = {"bad", "sad", "hate", "terrible", "poor", "awful", "negative", "horrible", "disappointing", "worst"}

def search_by_value(search_value, data_dict):
    matching_tweets=[]
    for x in range(0,len(data_dict)):
        if((data_dict[x]['text'].lower()).__contains__(search_value)):
            matching_tweets.append(data_dict[x])
    return  matching_tweets

def search_by_emotion(data_dict, search_keywords=['happy', 'sad']):
    new_mathched_tweets = []
    for i in range(0,len(data_dict)):
        if((data_dict[i]['text'].lower()).__contains__(search_keywords)):
            new_mathched_tweets.append(data_dict)
    return new_mathched_tweets

def search_by_location(location, data_dict):
    matching_tweets=[]

    for x in range(0,len(data_dict)):
        if(data_dict[x]['user']['location']!=None):
            if((data_dict[x]['user']['location'].lower()).__contains__(location)):
                matching_tweets.append(data_dict[x])
    return  matching_tweets


# Sorting Functions

def sort_by_followers(data_dict):
    accounts=[]
    sorted_list=sorted(data_dict,key=lambda a:get_followers(a),reverse=True) # sort by followers count, decreasingly  
    for tweet in sorted_list:
        accounts.append(tweet['user']['name'])

    # Convert each string in the array to a dictionary with a key
    json_array = [{"name": item} for item in accounts]

    # Convert the list of dictionaries to a JSON string
    array_size=len(json_array)
    if(array_size>0):
        if array_size>3:
            return json_array[:3]
        else:
            return json_array
    else:
        return []
    
def sort_by_retweet_count(data_dict):
    sorted_list=sorted(data_dict,key=lambda a:get_retweet(a),reverse=True) # sort by retweets count, decreasingly

    # Convert each string in the array to a dictionary with a key
    json_array = sorted_list

    # Convert the list of dictionaries to a JSON string
    array_size=len(json_array)
    if(array_size>0):
        if array_size>3:
            return json_array[:3]
        else:
            return json_array
    else:
        return []
 
def sort_by_country(data_dict):
    sorted_list=sorted(data_dict,key=lambda a:get_retweet(a),reverse=True) # sort by retweets count, decreasingly
    return sorted_list

# Comparators

def get_followers(data):
    return data['user']['followers_count'] # return the followers count of a tweet's user

def get_retweet(data):
    return data['retweet_count'] # return retweets of a tweet

def get_sentiment_analysis(tweet,positive_tweets_count,negative_tweets_count):

    for word in positive_words:
        if(tweet['text'].__contains__(word)):
            positive_tweets_count+=1
            return [positive_tweets_count,negative_tweets_count]

    for word in negative_words:
        if(tweet['text'].lower()).__contains__(word):
            negative_tweets_count+=1
            return [positive_tweets_count,negative_tweets_count]
    
    return [positive_tweets_count,negative_tweets_count]


def get_tweet_activity(tweet,sixtienth,seventieth):

    date=tweet['created_at'].split(' ')
    if(int(date[2])==16):
        sixtienth+=1
    else:
        seventieth+=1

    return [sixtienth,seventieth]
