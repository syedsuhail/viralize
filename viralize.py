import cli


from sys import argv
if __name__=='__main__':
    filename = argv[1]
else:
    filename='viral.ini'


data=cli.get_user_data(filename)
channels=['Twitter','Facebook','Email','gmail']


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
            from channels.smail import *
            gmail(dict1)
            print 'sent mail'
    else:
        print 'This app doesnt publish to %s'% dict1['channel']


