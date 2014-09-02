import viralize


def test_get_channels():
    channels= viralize.get_channels('channels/')
    assert channels[0].__name__ == 'channels.twitter_publish'




def test_viralize():
    data=[{'channel':'test','message':'hello'}]
    
    results=viralize.viralize(data)
    assert results
