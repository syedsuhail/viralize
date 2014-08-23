import cli


data=cli.get_user_data('scrap/viral.ini')
channels=['Twitter','Facebook','Email']

for dict1 in data:
    if dict1['channel'] in channels:
        if dict1['channel'] == 'Twitter':
            import channels.twit as twit
            t=twit.initialize()
            twit.pub_twit(dict1,t)
        elif dict1['channel']=='Facebook':
            import channels.fb as fb
            fb.pub_fb(dict1)
        elif dict1['channel']=='Email':
            import channels.smail
            print 'hello'
    else:
        print 'This app doesnt publish to %s'% dict1['channel']
