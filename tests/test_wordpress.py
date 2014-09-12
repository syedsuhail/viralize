from channels import wordpress_publish
import ConfigParser
import os
from wordpress_xmlrpc import Client, WordPressPost


wordpress = wordpress_publish.Wordpress_credential
assert wordpress == ".credentials"

def test_if_section():
    addres = "amvarish"
    pasw = "amvarish"
    user = "amvarish"
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    if not cfg.has_section('Wordpress'):
        cfg.add_section('Wordpress')
        cfg.set('Wordpress', 'Wordpressaddres', addres)
        cfg.set('Wordpress', 'password', pasw)
        cfg.set('Wordpress', 'username', user)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    ab,bc,cd = wordpress_publish.get_value()
    assert ab == addres + "/xmlrpc.php"
    assert bc == user
    assert cd == pasw
    
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    if cfg.has_section('Wordpress'):
        cfg.remove_section('Wordpress')
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    

def test_if_not_section():
    ab,bc,cd = wordpress_publish.get_value()
    ab = ab.decode('base64','strict');
    bc = bc.decode('base64','strict');
    cd = cd.decode('base64','strict');

    assert ab == "amvarish" + "/xmlrpc.php"
    assert bc == "amvarish"
    assert cd == "amvarish"


def test_if_file_not_exixt():
    if os.path.exists(wordpress):
        os.remove(wordpress)
    wordpress_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    ab = cfg.get('Wordpress', 'Wordpressaddres')
    bc = cfg.get('Wordpress', 'password')
    cd = cfg.get('Wordpress', 'username')
    ab = ab.decode('base64','strict');
    bc = bc.decode('base64','strict');
    cd = cd.decode('base64','strict');
    assert ab == "amvarish"
    assert bc == "amvarish"
    assert cd == "amvarish"


def test_if_option_not_exixt_in_file():
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    if cfg.has_section('Wordpress'):
        cfg.remove_section('Wordpress')
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    wordpress_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    ab = cfg.get('Wordpress', 'Wordpressaddres')
    bc = cfg.get('Wordpress', 'password')
    cd = cfg.get('Wordpress', 'username')
    assert ab == "YW12YXJpc2gveG1scnBjLnBocA=="
    assert bc == "YW12YXJpc2g="
    assert cd == "YW12YXJpc2g="
    if os.path.exists(wordpress):
        os.remove(wordpress)

def test_if_option_exist_in_file():
    addres = 'YW12YXJpc2gveG1scnBjLnBocA=='
    pasw = 'YW12YXJpc2g='
    user = 'YW12YXJpc2g='
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    if not cfg.has_section('Wordpress'):
        cfg.add_section('Wordpress')
        cfg.set('Wordpress', 'Wordpressaddres', addres)
        cfg.set('Wordpress', 'password', pasw)
        cfg.set('Wordpress', 'username', user)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    wordpress_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    ab = cfg.get('Wordpress', 'Wordpressaddres')
    bc = cfg.get('Wordpress', 'password')
    cd = cfg.get('Wordpress', 'username')
    assert ab == addres
    assert bc == pasw
    assert cd == user
    if os.path.exists(wordpress):
        os.remove(wordpress)

def object_has_created():
    addres = '36rahu'
    pasw = '36Kumbidi'
    user = 'rahul'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    if not cfg.has_section('Wordpress'):
        cfg.add_section('Wordpress')
        cfg.set('Wordpress', 'Wordpressaddres', addres)
        cfg.set('Wordpress', 'password', pasw)
        cfg.set('Wordpress', 'username', user)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    ab = wordpress_publish.initialise()
    cd = Client(addres, user, pasw)
    assert ab == cd
    if os.path.exists(wordpress):
        os.remove(wordpress)



def object_not_created():
    addres = '36rahu'
    user = 'rahul'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    if not cfg.has_section('Wordpress'):
        cfg.add_section('Wordpress')
        cfg.set('Wordpress', 'Wordpressaddres', addres)
        cfg.set('Wordpress', 'username', user)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    ab = wordpress_publish.initialise()
    assert ab == 'could not authenticate'
    if os.path.exists(wordpress):
        os.remove(wordpress)
    

def test_tittle():
    dict1 = {'title': 'wordpress_publish post throuh viralise'}
    mes = wordpress_publish.publish(dict1)
    assert mes == 'The tittle Should be in proper format'
    if os.path.exists(wordpress):
        os.remove(wordpress)


def test_tittle_empty():
    dict1 = {'tittle': ''}
    mes = wordpress_publish.publish(dict1)
    assert mes == 'The tittle could not create as empty'
    if os.path.exists(wordpress):
        os.remove(wordpress)


def test_message():
    dict1 = {'tittle': 'abc', 'messssage': 'This a wordpress_publish post from my app(viralise)'}
    mes = wordpress_publish.publish(dict1)
    assert mes == 'The message Should be in proper format'
    if os.path.exists(wordpress):
        os.remove(wordpress)


def test_message():
    dict1 = {'tittle': 'abc', 'message':''}
    mes = wordpress_publish.publish(dict1)
    assert mes == 'The message could not create as empty'
    if os.path.exists(wordpress):
        os.remove(wordpress)
