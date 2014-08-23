import flask
import tweepy
import ConfigParser
import appinfo

from flask import Flask
from flask import request


app = Flask(__name__)
session = dict()
Status = None


#Reciving application specific details
CONSUMER_TOKEN = appinfo.CONSUMER_TOKEN
CONSUMER_SECRET = appinfo.CONSUMER_SECRET
CALLBACK_URL = appinfo.CALLBACK_URL


 
@app.route("/")
def setup_twitter():
    #Creating auth object with usnig the cunsumer key and cunsumer token
    auth = tweepy.OAuthHandler(CONSUMER_TOKEN,
CONSUMER_SECRET,
CALLBACK_URL)
 
    print "Please authenticate our application....."

    try:
        redirect_url= auth.get_authorization_url()
        session['request_token']= (auth.request_token.key,auth.request_token.secret)
    except tweepy.TweepError:
        print 'Error! Failed to get request token'
 
    #rediect to authenticate application
    return flask.redirect(redirect_url)	
 

@app.route("/verify")
def verification():
 
    #checking for the verifiation
    verifier = request.args['oauth_verifier']
 
    auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
    token = session['request_token']
    del session['request_token']
    
    auth.set_request_token(token[0], token[1])
    
    #Creating the connection with the application
    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'
 
    #here check the authentication 
    api = tweepy.API(auth)

    try:
        api.me()
        Status = "Success"
    except tweepy.error.TweepError:
        Status = "Failed"
    
        
    #Save in a file for the next access        
    cfg = ConfigParser.RawConfigParser()
    cfg.read('.viralise')
    cfg.add_section('Twitter')
    cfg.set('Twitter', 'Token Key', auth.access_token.key)
    cfg.set('Twitter', 'Token Secret', auth.access_token.secret)
    cfg.set('Twitter','Status', Status)
    with open('.viralise', 'wb') as configfile:
        cfg.write(configfile)


    #Call for the tweet in the twitter account
    tweet()
    return "Now you can use our viralise app...Please check ur twitter account for the message tweet"
 

def tweet():

    
    cfg = ConfigParser.RawConfigParser()
    cfg.read('.viralise')
    if cfg.has_section('Twitter'):
        TOKEN = cfg.get('Twitter', 'Token Key')
        TOKEN_SEC = cfg.get('Twitter', 'Token Secret')
    auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
    
    auth.set_access_token(TOKEN,TOKEN_SEC)
    api = tweepy.API(auth)
    

    #recive the message from the controller
    message =  ''

    api.update_status(message)

 
def start():
    app.run()
