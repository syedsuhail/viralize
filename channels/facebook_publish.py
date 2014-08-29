import fbconsole


def publish(data):
    fbconsole.AUTH_SCOPE=['publish_stream']
    try:
        fbconsole.authenticate()
    except Exception:
        return 'Error: Could not authenticate'
    try:
        print data['message']
#        fbconsole.post('/me/feed', {'source':'Hello'})
        return 'Successfully posted message'
    except Exception:
        return 'Error: Could not post message'

#logging
#git filter-branch --tree 
#another object config
#too many . files
#return values
