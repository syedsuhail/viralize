from channels import twit

def test_twitter_publish():
    data={'message':'Hello','channel':'Twitter'}
    success = twit.twitter_publish(data)
    assert success == 1
