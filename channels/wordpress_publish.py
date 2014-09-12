import os
import ConfigParser
import viralize

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
            Wordpress_id = Wordpress_id + "/xmlrpc.php"
            return Wordpress_id,username,password
        except ConfigParser.NoOptionError:
            raise Error
    else:
        Wordpress_id = viralize.get_data('Wordpress address')
        username = viralize.get_data('Wordpress username')
        password = viralize.get_data('Wordpress password')
        Wordpress_id = Wordpress_id + "/xmlrpc.php"
        return Wordpress_id,username,password

        

def initialise():
    cfg = ConfigParser.RawConfigParser()
    
    #Creates if there no exist an credential file 
    if not os.path.exists(Wordpress_credential):
        cfg.read(Wordpress_credential)
        cfg.add_section('Wordpress')
        Wordpress_id,username, password = get_value()
        cfg.set('Wordpress', 'Wordpressaddres', username)
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
            Wordpress_id = cfg.get('Wordpress', 'Wordpressaddres')
            username = cfg.get('Wordpress', 'username')
            password = cfg.get('Wordpress', 'password')
    try:
	#creates an wordpress object
        wp = Client(Wordpress_id, username, password)
        return wp
    except Exception:
        return 'could not authenticate'



    
def publish():
    wp=initialize()
    post = WordPressPost()
    #Checks tittle is exist
    if not data['tittle']:
        return 'The tittle could not create as empty'
    else:
        post.title = data['tittle']
    #checks message is exist
    if not data['message']:
        return 'The message could not create as empty'
    else:
        post.content = data['message']
    post.terms_names = {'post_tag': ['test', 'firstpost'],'category': ['Introductions', 'Tests']}
    post.post_status = 'publish'
    #trying in to post on the wordpress
    try:
        wp.call(NewPost(post))
        return 'Published the message in wordpress succesfully..'
    except Exception:
        return 'Could not publish'
