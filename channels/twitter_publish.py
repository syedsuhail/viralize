from twitter import *
import os
import viralize


def publish(data):
    CONSUMER_KEY='PioawmiVQLIGSQCdLfN8wbgnJ'
    CONSUMER_SECRET='41SHzZ6uAGZoVGPCXGC3mPlZmzCan0m30xYvOK0EjdfZEJRFs1'
    MY_TWITTER_CREDS = os.path.expanduser('.tcredentials')
    if not os.path.exists(MY_TWITTER_CREDS):
        oauth_dance("Viralise", CONSUMER_KEY, CONSUMER_SECRET,
                    MY_TWITTER_CREDS)

    oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
    try:
        t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))
    except Exception:
        return "Check your internet connection or the credential file has been crashed"

    if 'message' in data:
        if data['message'] != '':
            message = data['message']
        else:
            msg = "Do you want to continue as message in twitter as empty(yes/no):"
            request = "Twitter message"
            y,value = viralize.warning(msg,request)
            if  y == 'no' or y == 'NO' or y == 'No':
                message = value
            elif y == 'yes' or y == 'YES' or y == 'Yes':
                return 'Twitter Cannot post the blank message'
            else:
                return 'Wrong option is given'
    else: 
        return 'The input in mail (message) may be wrong. Check your input methode'

    if len(message) > 140:
         return "Message is %s long twitter only post 140 character" %len(message)
    else:
        try:
            t.statuses.update(status=message)
            return 'Successfully sent to Twitter'
        except:
            return 'Error: Could not post to twitter'
