import fbconsole
import cli

def fb_publish(data):
    fbconsole.AUTH_SCOPE=['publish_stream']
    try:
        fbconsole.authenticate()
    except Exception:
        return "Could not authenticate"
    try:
        print data['message']
#        fbconsole.post('/me/feed', {'source':'Hello'})
        cli.show_info('Successfuly sent to fb')
        return 1
    except Exception:
        cli.show_info(unsuccessful)
        return None

