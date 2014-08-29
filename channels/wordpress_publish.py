import ConfigParser
import os
import cli
from getpass import getpass
from binascii import hexlify, unhexlify
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost

def initialize():
    MY_BLOG_CREDS = os.path.expanduser('.wordpress_credentials')
    if not os.path.exists(MY_BLOG_CREDS):
        blog_id = raw_input("Enter Blog addres (http://mysite.wordpress.com):")
        blog_id = blog_id + "/xmlrpc.php"
        username,password = cli.get_username_pass('Wordpress')
        username = unhexlify(username)
        password = unhexlify(password)
        cfg = ConfigParser.RawConfigParser()
        cfg.read('.my_blog_credentials')
        cfg.add_section('Wordpress')
        cfg.set('Wordpress', 'Blogaddres', blog_id)
        cfg.set('Wordpress', 'Username', username)
        cfg.set('Wordpress', 'Password', password)
        with open('.wordpress_credentials', 'wb') as configfile:
            cfg.write(configfile)
    else:
        cfg = ConfigParser.RawConfigParser()
        cfg.read('.wordpress_credentials')
        if cfg.has_section('Wordpress'):
            blog_id = cfg.get('Wordpress', 'Blogaddres')
            username = unhexlify(cfg.get('Wordpress', 'Username'))
            password = unhexlify(cfg.get('Wordpress', 'Password'))
    try:
        wp = Client(blog_id, username, password)
        return wp
    except Exception:
        cli.show_info('could not authenticate')
        return None

    

def publish(data):
    wp=initialize()
    if wp == None:
        return None
    post = WordPressPost()
    post.title = data['tittle']
    post.content = data['message']
    post.terms_names = {'post_tag': ['test', 'firstpost'],'category': ['Introductions', 'Tests']}
    post.post_status = 'publish'
    try:
        wp.call(NewPost(post))
        cli.show_info( "Published the message in wordpress succesfully..")
        return 1
    except Exception:
        cli.show_info("Could not publish")
        return None
