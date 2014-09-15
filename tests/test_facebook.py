import ConfigParser
import os
from channels import facebook_publish

MY_TWITTER_CREDS = os.path.expanduser('.fb_access_token')

def test_reading():
    abc = 'helllo'
    cfg = ConfigParser.RawConfigParser()
    cfg.read('.fb_access_token')
    if not cfg.has_section('abcd'):
        cfg.add_section('abcd')
        cfg.set('abcd', 'akjjkan', abc)
    with open('.fb_access_token', 'wb') as configfile:
        cfg.write(configfile)
    data={'channel':'test','message':'hello'}
    ab = facebook_publish.publish(data)
    assert ab == 'Error: Could not authenticate' 
    if os.path.exists('.fb_access_token'):
        os.remove('.fb_access_token')


def test_message_null():
    fh = open(MY_TWITTER_CREDS,"w")
    fh.write('{"access_token": "CAACjeiZB6FgIBAG5JZC5jQMQCl5KKHrqduQLrcV801t3EpHnx7LAZBBZBk0AYM5j36ywmCgQTh4M1fXcT2DxxhIFIpZCkzRVZCXlEbaqN4fJ3rdmG1OYIEg5cvvDYoGrPB0X8BwddVZCZC8br7pUDjZCLvmZBQaZC6GTx32I4swfuZCggwEAD0xikU8HVh9ZAMPHRjc5p7ZAomnAidEIwH86Td6mxF", "scope": ["publish_stream"], "expires_at": 1410814800}')
    fh.close()
    data={'channel':'test'}
    ab = facebook_publish.publish(data)
    assert ab == 'The input in Facebook (message) may be wrong. Check your input methode' 
    if os.path.exists('.fb_access_token'):
        os.remove('.fb_access_token')
    
def test_message_empty():
    fh = open(MY_TWITTER_CREDS,"w")
    fh.write('{"access_token": "CAACjeiZB6FgIBAG5JZC5jQMQCl5KKHrqduQLrcV801t3EpHnx7LAZBBZBk0AYM5j36ywmCgQTh4M1fXcT2DxxhIFIpZCkzRVZCXlEbaqN4fJ3rdmG1OYIEg5cvvDYoGrPB0X8BwddVZCZC8br7pUDjZCLvmZBQaZC6GTx32I4swfuZCggwEAD0xikU8HVh9ZAMPHRjc5p7ZAomnAidEIwH86Td6mxF", "scope": ["publish_stream"], "expires_at": 1410814800}')
    fh.close()
    data={'channel':'test','message':''}
    ab = facebook_publish.publish(data)
    assert ab == 'Facebook Cannot post the blank message' 
    if os.path.exists('.fb_access_token'):
        os.remove('.fb_access_token')
