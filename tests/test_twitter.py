from channels import twitter_publish
import os
import ConfigParser
import __builtin__
import twitter
MY_TWITTER_CREDS = os.path.expanduser('.tcredentials')

def test_reading(monkeypatch):
    abc = 'helllo'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(MY_TWITTER_CREDS)
    if not cfg.has_section('abcd'):
        cfg.add_section('abcd')
        cfg.set('abcd', 'akjjkan', abc)
    with open('.tcredentials', 'wb') as configfile:
        cfg.write(configfile)
    data={'channel':'test','message':'hello'}
    def mock_twitter():
        return 'helloo';
    monkeypatch.setattr(twitter, 'Twitter', mock_twitter)
    def mock_read_token():
        return 'hai';
    monkeypatch.setattr(twitter, 'read_token_file', mock_read_token)
    ab = twitter_publish.publish(data)
    assert ab == 'Error: Could not post to twitter' 
    if os.path.exists(MY_TWITTER_CREDS):
        os.remove(MY_TWITTER_CREDS)

def test_message_not_exist():
    abc = 'helllo'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(MY_TWITTER_CREDS)
    if not cfg.has_section('abcd'):
        cfg.add_section('abcd')
        cfg.set('abcd', 'akjjkan', abc)
    with open('.tcredentials', 'wb') as configfile:
        cfg.write(configfile)
    data={'channel':'test','messddage':''}
    ab = twitter_publish.publish(data)
    assert ab == 'The input in twitter (message) may be wrong. Check your input methode' 
    if os.path.exists(MY_TWITTER_CREDS):
        os.remove(MY_TWITTER_CREDS)



def test_message_empty(monkeypatch):
    abc = 'helllo'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(MY_TWITTER_CREDS)
    if not cfg.has_section('abcd'):
        cfg.add_section('abcd')
        cfg.set('abcd', 'akjjkan', abc)
    with open('.tcredentials', 'wb') as configfile:
        cfg.write(configfile)
    data={'channel':'test','message':''}
    ab = twitter_publish.publish(data)
    assert ab == 'Twitter Cannot post the blank message' 
    if os.path.exists(MY_TWITTER_CREDS):
        os.remove(MY_TWITTER_CREDS)

def test_140_charcter():
    abc = 'helllo'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(MY_TWITTER_CREDS)
    if not cfg.has_section('abcd'):
        cfg.add_section('abcd')
        cfg.set('abcd', 'akjjkan', abc)
    with open('.tcredentials', 'wb') as configfile:
        cfg.write(configfile)
    data={'channel':'test','message':'aankjsndkfbsfnmnfnms mnmbjzvcjc mc nbcznzn,m ,mzbm ,nznkjzkcj jhk sacakjkamcbjh  skjbksbvv  kjbkjsnknv jsk schb s skj sbjsbks ksk kvs hskjnk sv skksj ns snkjsks  sjnksb kajsnk'}
    ab = twitter_publish.publish(data)
    assert ab == 'Message is 175 long twitter only post 140 character' 
    if os.path.exists(MY_TWITTER_CREDS):
        os.remove(MY_TWITTER_CREDS)

