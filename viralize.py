import cli




def viralize():
    filename= cli.get_filename()
    data=cli.get_user_data(filename)
    channels=['Twitter','Facebook','Email','gmail','Wordpress']
    success={}
    for dict1 in data:
        if dict1['channel'] in channels:
            if dict1['channel'] == 'Twitter':
                import channels.twit as twit
                success['Twitter']=twit.twitter_publish(dict1)
            elif dict1['channel'] == 'Wordpress':
                import channels.blog as blog
                wp=blog.initialize()
                success['Blog']=blog.wordpress_publish(dict1,wp)
            elif dict1['channel']=='Facebook':
                import channels.fb as fb
                success['facebook'] = fb.fb_publish(dict1)
            elif dict1['channel']=='Email':
                from channels.smail import *
                success['email'] = gmail(dict1)
    
                    
        else:
            print 'This app doesnt publish to %s'% dict1['channel']
    print success


if __name__=='__main__':
    viralize()
