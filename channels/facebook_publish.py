import fbconsole
import controller

'''Recives tokens from the credential file and trying to post on facebook account and return the status message'''
def publish(data):
    fbconsole.AUTH_SCOPE=['publish_stream']
    try:
        fbconsole.authenticate()
    except Exception:
        return 'Error: Could not authenticate'
    

    if 'message' in data:
        if data['message'] != '':
            message = data['message']
        else:
            msg = "Do you want to continue as message in facebook as empty(yes/no):"
            request = "Facebook message"
            y,value = controller.warning(msg,request)
            if  y == 'no' or y == 'NO' or y == 'No':
                message = value
            elif y == 'yes' or y == 'YES' or y == 'Yes':
                return 'Facebook Cannot post the blank message'
            else:
                return 'Wrong option is given'
    else: 
        return 'The input in Facebook (message) may be wrong. Check your input methode'

    try:
        fbconsole.post('/me/feed', {'message':message})
        return 'Successfully posted message'
    except Exception:
        return 'Error: Could not post message'
