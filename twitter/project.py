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

# store the value headers
sex_column = df['sex']
race_column = df['race']
age_column = df['age']
city_column = df['city']
susp_column = df['suspicion']
action_column = df['action']

j = 0 # index for forloop

# sort DF by date
# df.sort('date')

# convert date object into datetime object at midnight
for date in date_column:
    datetime.combine(date, datetime.min.time())

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
        sex = df.get_value(j, sex_column)
        race = df.get_value(j, race_column)
        age = df.get_value(j, age_column)
        city = df.get_value(j, city_column)
        action = df.get_value(j, action_column)
        suspicion = df.get_value(j, susp_column)

        # Prepare tweet
        tweet = "Today: " + date + ", Police " + action + " a " + age + "-year-old " + race + " " + sex + " in " + city + ". Citing: " + suspicion
        print(tweet)
        api.update_status(line)
        sleep(900)
