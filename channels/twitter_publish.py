from twitter import *
import os
import controller


def publish(data):
    '''Recives tokens from the credential file and trying to tweet on twiter account and return the status message'''
    CONSUMER_KEY='PioawmiVQLIGSQCdLfN8wbgnJ'
    CONSUMER_SECRET='41SHzZ6uAGZoVGPCXGC3mPlZmzCan0m30xYvOK0EjdfZEJRFs1'
    MY_TWITTER_CREDS = os.path.expanduser('.tcredentials')
    if not os.path.exists(MY_TWITTER_CREDS):
        oauth_dance("Viralise", CONSUMER_KEY, CONSUMER_SECRET,
                    MY_TWITTER_CREDS)

    try:
        oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
    except Exception:
        return 'The redential file has been crashed'
        
    try:
        t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))
    except Exception:
        return "Check your internet connection "

    if 'message' in data:
        if data['message'] != '':
            message = data['message']
        else:
            return 'Twitter Cannot post the blank message'
    else: 
        return 'The input in twitter (message) may be wrong. Check your input methode'

    if len(message) > 140:
         return "Message is %s long twitter only post 140 character" %len(message)
    else:
        try:
            t.statuses.update(status=message)
            return 'Successfully sent to Twitter'
        except:
            return 'Error: Could not post to twitter'
