import os
import ConfigParser
import viralize
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost


Wordpress_credential = os.path.expanduser('.credentials')

'''Returns the Wordpress address'''
def get_value():
    Wordpress_credential = os.path.expanduser('.credentials')
    cfg = ConfigParser.RawConfigParser()
    cfg.read(Wordpress_credential)
    #Wordpress address taken from the credential file
    if cfg.has_section('Wordpress'):
        try:
            Wordpress_id = cfg.get('Wordpress', 'Wordpressaddres')
            password = cfg.get('Wordpress', 'password')
            username = cfg.get('Wordpress', 'username')
            return Wordpress_id,username,password
        except ConfigParser.NoOptionError:
            raise Error
    #Values taken as user input
    else:
        Wordpress_id = viralize.get_data('Wordpress address')
        username = viralize.get_data('Wordpress username')
        password = viralize.get_password('Wordpress password')
        Wordpress_id = Wordpress_id + "/xmlrpc.php"
        Wordpress_id = Wordpress_id.encode('base64','strict');
        username = username.encode('base64','strict');
        password = password.encode('base64','strict');
        return Wordpress_id,username,password


def initialise():
    cfg = ConfigParser.RawConfigParser()
    #Creates if there no exist an credential file
    if not os.path.exists(Wordpress_credential):
        cfg.read(Wordpress_credential)
        cfg.add_section('Wordpress')
        Wordpress_id,username, password = get_value()
        cfg.set('Wordpress', 'Wordpressaddres', Wordpress_id)
        cfg.set('Wordpress', 'username', username)
        cfg.set('Wordpress', 'password', password)
        with open('.credentials', 'wb') as configfile:
            cfg.write(configfile)
            #Read from the credential file
    else:
        cfg.read(Wordpress_credential)
        #Put Values in to the credential file
        if not cfg.has_section('Wordpress'):
            cfg.add_section('Wordpress')
            Wordpress_id,username, password = get_value()
            cfg.set('Wordpress', 'Wordpressaddres', Wordpress_id)
            cfg.set('Wordpress', 'username', username)
            cfg.set('Wordpress', 'password', password)
            with open('.credentials', 'wb') as configfile:
                cfg.write(configfile)
        else:
            #Takes values from the credential file
            Wordpress_id,username, password = get_value()
    

    Wordpress_id = Wordpress_id.decode('base64','strict'); 
    username = username.decode('base64','strict'); 
    password = password.decode('base64','strict');
            
    try:
        #creates an wordpress object
        wp = Client(Wordpress_id, username, password)
        return wp
    except Exception:
        return "Check your internet connection"

def publish(data):
    wp = initialise()
    post = WordPressPost()
    #Checks tittle is exist
    if 'tittle' in data:
        if data['tittle'] != '':
            post.title = data['tittle']
        else:
            msg = "Do you want to continue as tittle in wordpress as empty(yes/no):"
            request = "Wordpress tittle"
            y,value = viralize.warning(msg,request)
            if  y != 'abcd':
                message = value
            else:
                return 'Given option is wrong:'

    else:
        return 'The tittle Should be in proper format'
    
    #checks message is exist
    if 'message' in data:
        if data['message'] != '':
            post.content = data['message']
        else:
            return 'The message in wordpress could not create as empty'
    else:
        return 'The message Should be in proper format'
    
    post.terms_names = {'post_tag': ['test', 'firstpost'],'category': ['Introductions', 'Tests']}
    post.post_status = 'publish'

    #trying in to post on the wordpress
    try:
        wp.call(NewPost(post))
        return 'Published the message in wordpress succesfully..'
    except Exception:
        return 'Could not publish'
        
