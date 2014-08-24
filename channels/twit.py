from twitter import *
import os

def initialize():
    CONSUMER_KEY='PioawmiVQLIGSQCdLfN8wbgnJ'
    CONSUMER_SECRET='41SHzZ6uAGZoVGPCXGC3mPlZmzCan0m30xYvOK0EjdfZEJRFs1'
    MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
    if not os.path.exists(MY_TWITTER_CREDS):
        oauth_dance("Viralise", CONSUMER_KEY, CONSUMER_SECRET,
                    MY_TWITTER_CREDS)

    oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

    t = Twitter(auth=OAuth(
                oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

    return t


def pub_twit(data,t):
    print data['message']
    t=initialize()
    time=t.statuses.home_timeline()
    print time[0]['user']['screen_name']

