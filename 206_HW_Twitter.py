import unittest
import tweepy
import requests
import json
from pprint import pprint


## SI 206 - HW
## COMMENT WITH:
## Your section day/time: Thursday 6-7 PM
## Any names of people you worked with on this assignment:


## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points

consumer_key = "d1EzdlshnY1EetH7wOuMPZIos"
consumer_secret = "frQX4bi4gG28giPbeZo7uBmt9BfQ6awL4Hb38Cpb85rIW8DSEL"
access_token = "817142552067506176-EMzBT7YXKbbWXpx3RYLPEhy4MZkmoFZ"
access_token_secret = "FMdkuKyJsaXSrgXKvwNDIQozt4xiivuosm57QZEivVQnW"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) 

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except 
## 		statement shown in class.
CACHE_FNAME = "206_HW7_Twitter_cache.json" #creating and naming cache file
try:
    cache_file = open(CACHE_FNAME, 'r') #attempting to read data from the file
    cache_contents = cache_file.read() #if it can read data from the file, it converts the data to a string
    cache_file.close() #closing the file
    CACHE_DICTIONARY = json.loads(cache_contents) #adding data to cache dictionary
except:
    CACHE_DICTIONARY = {}



## 2. Write a function to get twitter data that works with the caching pattern, 
## 		so it either gets new data or caches data, depending upon what the input 
##		to search for is. 
def get_twitter_data(x):
    if x in CACHE_DICTIONARY: 
        print ('using cache') #using cache file if it's already cached in the cache dictionary
        return CACHE_DICTIONARY[x] #return the dictionary correlated to whatever term 'x' is searched 
    else:
        print ('fetching') #if not already cached in the cache dictionary, 
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
        tweets = api.search(x)
        twitter_data = {} #create empty dictionary called twitter_data
        for tweet in tweets['statuses']:
            twitter_data[tweet['text']] = tweet['created_at']
        CACHE_DICTIONARY[x] = twitter_data #adding a dictionary to the already existing cache_dictionary
        write_file = open(CACHE_FNAME, 'w')
        write_file.write(json.dumps(CACHE_DICTIONARY)) #writing the cache_dictionary to the cache file 206_HW7_Twitter_cache.json
        write_file.close()
    return twitter_data

## 3. Using a loop, invoke your function, save the return value in a variable, and explore the 
##		data you got back!


## 4. With what you learn from the data -- e.g. how exactly to find the 
##		text of each tweet in the big nested structure -- write code to print out 
## 		content from 5 tweets, as shown in the linked example.

my_input = input("Enter tweet term: ") #creating the input in which I will search for a specific term on Twitter
my_data = get_twitter_data(my_input)
t = 0
for y in my_data.keys(): #looping through the keys of my_data
    if (t < 5):
        print ('TEXT: ' + y) #printing the text and the associated key
        print ('CREATED AT: ' + my_data[y]) #printing when the tweet was created, and its associated value
        print ('\n') #new line
        t += 1







