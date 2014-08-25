import ConfigParser
import os
from getpass import getpass
from binascii import hexlify, unhexlify
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost

def initialize():
    MY_BLOG_CREDS = os.path.expanduser('.my_blog_credentials')
    if not os.path.exists(MY_BLOG_CREDS):
        blog_id = raw_input("Enter Blog addres (http://mysite.wordpress.com):")
        blog_id = blog_id + "/xmlrpc.php"
        username = hexlify(raw_input('Enter Blog username :'))
        password = hexlify(getpass('Enter Blog Password :'))
        cfg = ConfigParser.RawConfigParser()
        cfg.read('.my_blog_credentials')
        cfg.add_section('Blog')
        cfg.set('Blog', 'Blogaddres', blog_id)
        cfg.set('Blog', 'Username', username)
        cfg.set('Blog', 'Password', password)
        with open('.my_blog_credentials', 'wb') as configfile:
            cfg.write(configfile)
    else:
        cfg = ConfigParser.RawConfigParser()
        cfg.read('.my_blog_credentials')
        if cfg.has_section('Blog'):
            blog_id = cfg.get('Blog', 'Blogaddres')
            username = unhexlify(cfg.get('Blog', 'Username'))
            password = unhexlify(cfg.get('Blog', 'Password'))

    wp = Client(blog_id, username, password)

    return wp

def pub_blog(data,wp):
    wp=initialize()
    post = WordPressPost()
    post.title = data['tittle']
    post.content = data['message']
    post.terms_names = {'post_tag': ['test', 'firstpost'],'category': ['Introductions', 'Tests']}
    post.post_status = 'publish'
    wp.call(NewPost(post))
    print "Published the message in blog succesfully.."
