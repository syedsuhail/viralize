import fbconsole


def pub_fb(data):
    fbconsole.AUTH_SCOPE=['publish_stream']
    fbconsole.authenticate()
    print data['message']
