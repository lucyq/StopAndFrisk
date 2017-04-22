#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys
import config
import pandas as pd
from datetime import date
from datetime import datetime

# Twitter auth info
CONSUMER_KEY = config.consumer_key
CONSUMER_SECRET = config.consumer_secret
ACCESS_KEY = config.access_token
ACCESS_SECRET = config.access_token_secret

# Authenticate
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Import our CSV - using sample CSV for now
df = pd.read_csv("data.csv")
date_column = df['date']
date_column = pd.to_datetime(df.date)
city_column = df['city']

j = 0 # index for forloop

# sort DF by date
# df.sort('date')

# convert date object into datetime object at midnight
# for date in date_column:
#     datetime.combine(date, datetime.min.time())

# convert cities to lower case, and then to CamelCase
for cities in str(city_column):
    cities = cities.lower()

# Time management
# If for some reason this script is still running
# after a year, we'll stop after 365 days
for date in date_column:
    for i in xrange(0,365):
        # sleep until midnight
        # t = datetime.datetime.today()
        # future = datetime.datetime(date)
        # if t.hour >= 0:
        #     future += datetime.timedelta(days=1) #calculate future date
        # time.sleep((future-t).seconds) # sleep for d(future/today) time

        # wake up and do midnight stuff

        # lets get all of our values here
        sex = df.get_value(j, 'sex')
        race = df.get_value(j, 'race')
        age = df.get_value(j, 'age')
        city = df.get_value(j, 'city')
        action = df.get_value(j, 'action')
        suspicion = df.get_value(j, 'suspicion')

        # Prepare tweet
        tweet = "Today: " + str(date) + ", Police " + str(action) + " a " + str(int(age)) + "-year-old " + str(race) + " " + str(sex) + " in " + str(city).title() + ". Citing: " + suspicion
        print(tweet)
        api.update_status(tweet)
        print("sleeping for 15 minutes to test if this thing works...")
        time.sleep(900)

        j += 1
