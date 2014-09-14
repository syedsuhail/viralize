from controller import get_channels,viralize


def test_get_channels():
    channels= get_channels('channels/')
    assert channels[0].__name__ == 'channels.twitter_publish'




def test_viralize():
    data=[{'channel':'test','message':'hello'}]
    
    results=viralize(data)
    assert results
