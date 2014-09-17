from channels import wordpress_publish
import ConfigParser
import os
import __builtin__
import getpass
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
    assert ab == addres
    assert bc == user
    assert cd == pasw
    
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    if cfg.has_section('Wordpress'):
        cfg.remove_section('Wordpress')
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    

def test_value_not_exist(monkeypatch):
    def mock_raw_input(*args, **kwargs):
        return 'yolo';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    ab,bc,cd = wordpress_publish.get_value()
    ab = ab.decode('base64','strict');
    bc = bc.decode('base64','strict');
    cd = cd.decode('base64','strict');
    
    assert bc == "yolo"
    assert ab == "yolo" + "/xmlrpc.php"
    assert cd == "yolo"


def test_if_file_not_exixt(monkeypatch):
    if os.path.exists(wordpress):
        os.remove(wordpress)
    def mock_raw_input(*args, **kwargs):
        return 'yolo';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    wordpress_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    ab = cfg.get('Wordpress', 'Wordpressaddres')
    bc = cfg.get('Wordpress', 'password')
    cd = cfg.get('Wordpress', 'username')
    ab = ab.decode('base64','strict');
    bc = bc.decode('base64','strict');
    cd = cd.decode('base64','strict');
    assert ab == "yolo/xmlrpc.php"
    assert bc == "yolo"
    assert cd == "yolo"


def test_if_option_not_exixt_in_file(monkeypatch):
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    if cfg.has_section('Wordpress'):
        cfg.remove_section('Wordpress')
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    def mock_raw_input(*args, **kwargs):
        return 'yolo';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    wordpress_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(wordpress)
    ab = cfg.get('Wordpress', 'Wordpressaddres')
    bc = cfg.get('Wordpress', 'password')
    cd = cfg.get('Wordpress', 'username')
    ab = ab.decode('base64','strict');
    bc = bc.decode('base64','strict');
    cd = cd.decode('base64','strict');
    assert ab == "yolo/xmlrpc.php"
    assert bc == "yolo"
    assert cd == "yolo"

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
    addres = 'ajbmcxnndv'
    pasw = 'kjfkjnsdkjnd'
    user = 'DJNkjndkla'
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
    addres = 'nlknal'
    user = 'snlksmkms'
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
    

def test_tittle(monkeypatch):
    dict1 = {'title': 'wordpress_publish post throuh viralise','message':'hajab'}
    def mock_raw_input(*args, **kwargs):
        return 'yolo';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = wordpress_publish.publish(dict1)
    assert mes == 'The input in wordpress (tittle) may be wrong. Check your input methode'
    if os.path.exists(wordpress):
        os.remove(wordpress)


def test_tittle_empty(monkeypatch):
    dict1 = {'tittle':'','message':'dskjnjs'}
    def mock_raw_input(*args, **kwargs):
        return 'yolo';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = wordpress_publish.publish(dict1)
    assert mes == 'Given option is wrong:'
    if os.path.exists(wordpress):
        os.remove(wordpress)


def test_message(monkeypatch):
    dict1 = {'tittle': 'abc', 'messssage': 'This a wordpress_publish post from my app(viralise)'}
    def mock_raw_input(*args, **kwargs):
        return 'yolo';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = wordpress_publish.publish(dict1)
    assert mes == 'The input in wordpress (message) may be wrong. Check your input methode'
    if os.path.exists(wordpress):
        os.remove(wordpress)


def test_message_2(monkeypatch):
    dict1 = {'tittle': 'abc', 'message':''}
    def mock_raw_input(*args, **kwargs):
        return 'yolo';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = wordpress_publish.publish(dict1)
    assert mes == 'The message in wordpress could not create as empty'
    if os.path.exists(wordpress):
        os.remove(wordpress)
