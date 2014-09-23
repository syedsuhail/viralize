import fbconsole
import controller


def publish(data):
    '''Recives tokens from the credential file and trying to post on facebook account and return the status message'''
    fbconsole.AUTH_SCOPE=['publish_stream']
    try:
        fbconsole.authenticate()
    except Exception:
        return 'Error: Could not authenticate'
    

    if 'message' in data:
        if data['message'] != '':
            message = data['message']
        else:
            return 'Facebook Cannot post the blank message'
    else: 
        return 'The input in Facebook (message) may be wrong. Check your input methode'

    try:
        fbconsole.post('/me/feed', {'message':message})
        return 'Successfully posted message'
    except Exception:
        return 'Error: Could not post message'
