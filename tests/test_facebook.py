import ConfigParser
import os
import __builtin__
import fbconsole
from channels import facebook_publish



def test_reading(monkeypatch):
    data={'channel':'test','message':'hello'}
    def mock_raw_input(*args, **kwargs):
        return 'yes';
    monkeypatch.setattr(fbconsole, 'authenticate', mock_raw_input)
    ab = facebook_publish.publish(data)
    assert ab == 'Error: Could not post message' 


def test_message_null(monkeypatch):
    data={'channel':'test'}
    def mock_raw_input(*args, **kwargs):
        return 'yes';
    def mock_raw_input(*args, **kwargs):
        return 'yes';
    monkeypatch.setattr(fbconsole, 'authenticate', mock_raw_input)
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    ab = facebook_publish.publish(data)
    assert ab == 'The input in Facebook (message) may be wrong. Check your input methode' 
    
    
def test_message_empty(monkeypatch):
    data={'channel':'test','message':''}
    def mock_raw_input(*args, **kwargs):
        return 'yes';
    def mock_raw_input(*args, **kwargs):
        return 'yes';
    monkeypatch.setattr(fbconsole, 'authenticate', mock_raw_input)
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    ab = facebook_publish.publish(data)
    assert ab == 'Facebook Cannot post the blank message' 

