import controller


def test_get_channels():
    channels = controller.get_channels('/home/chicku/viralize/channels/')
    assert channels[0].__name__ == 'channels.facebook_publish'




def test_viralize():
    data=[{'channel':'test','message':'hello'}]
    
    results = controller.viralize(data)
    assert results == {}
