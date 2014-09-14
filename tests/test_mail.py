from channels import email_publish
import ConfigParser
import os


mail = email_publish.mail_credential
assert mail == ".credentials"

def test_if_section():
    addres = "amvarish"
    pasw = "amvarish"
    user = "amvarish"
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if not cfg.has_section('mail'):
        cfg.add_section('mail')
        cfg.set('mail', 'mailaddres', addres)
        cfg.set('mail', 'password', pasw)
        cfg.set('mail', 'username', user)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    ab,bc,cd = email_publish.get_value()
    assert ab == addres
    assert bc == user
    assert cd == pasw
    
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if cfg.has_section('mail'):
        cfg.remove_section('mail')
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    

def test_if_not_section():
    ab,bc,cd = email_publish.get_value()
    ab = ab.decode('base64','strict');
    bc = bc.decode('base64','strict');
    cd = cd.decode('base64','strict');

    assert ab == "amvarish"
    assert bc == "amvarish"
    assert cd == "amvarish"


def test_if_file_not_exixt():
    if os.path.exists(mail):
        os.remove(mail)
    email_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    ab = cfg.get('mail', 'mailaddres')
    bc = cfg.get('mail', 'password')
    cd = cfg.get('mail', 'username')
    ab = ab.decode('base64','strict');
    bc = bc.decode('base64','strict');
    cd = cd.decode('base64','strict');
    assert ab == "amvarish"
    assert bc == "amvarish"
    assert cd == "amvarish"


def test_if_option_not_exixt_in_file():
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if cfg.has_section('mail'):
        cfg.remove_section('mail')
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    email_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    ab = cfg.get('mail', 'mailaddres')
    bc = cfg.get('mail', 'password')
    cd = cfg.get('mail', 'username')
    assert ab == "YW12YXJpc2g="
    assert bc == "YW12YXJpc2g="
    assert cd == "YW12YXJpc2g="
    if os.path.exists(mail):
        os.remove(mail)

def test_if_option_exist_in_file():
    addres = 'YW12YXJpc2g='
    pasw = 'YW12YXJpc2g='
    user = 'YW12YXJpc2g='
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if not cfg.has_section('mail'):
        cfg.add_section('mail')
        cfg.set('mail', 'mailaddres', addres)
        cfg.set('mail', 'password', pasw)
        cfg.set('mail', 'username', user)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    email_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    ab = cfg.get('mail', 'mailaddres')
    bc = cfg.get('mail', 'password')
    cd = cfg.get('mail', 'username')
    assert ab == addres
    assert bc == pasw
    assert cd == user
    if os.path.exists(mail):
        os.remove(mail)

def object_has_created():
    addres = '36rahu'
    pasw = '36Kumbidi'
    user = 'rahul'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if not cfg.has_section('mail'):
        cfg.add_section('mail')
        cfg.set('mail', 'mailaddres', addres)
        cfg.set('mail', 'password', pasw)
        cfg.set('mail', 'username', user)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    ab = email_publish.initialise()
    cd = Client(addres, user, pasw)
    assert ab == cd
    if os.path.exists(mail):
        os.remove(mail)


def test_to_address():
    dict1 = {'toac': 'abc', 'message':'abcd'}
    mes = email_publish.publish(dict1)
    assert mes == 'The to address Should be in proper format'
    if os.path.exists(mail):
        os.remove(mail)

def test_to_address_empty():
    dict1 = {'to':'', 'message':'abcd'}
    mes = email_publish.publish(dict1)
    assert mes == 'The to address could not create as empty'
    if os.path.exists(mail):
        os.remove(mail)

def test_message():
    dict1 = {'to': 'abc', 'messsage':'abcd'}
    mes = email_publish.publish(dict1)
    assert mes == 'The message Should be in proper format'
    if os.path.exists(mail):
        os.remove(mail)


def test_message_empty():
    dict1 = {'to': 'abc', 'message':''}
    mes = email_publish.publish(dict1)
    assert mes == 'The message could not create as empty'
    if os.path.exists(mail):
        os.remove(mail)

def test_subject():
    dict1 = {'to': 'abc', 'message':'abcd','subjbect':'abcd'}
    mes = email_publish.publish(dict1)
    assert mes == 'The subject Should be in proper format'
    if os.path.exists(mail):
        os.remove(mail)


def test_subject_empty():
    dict1 = {'to': 'abc', 'message':'abcd','subject':''}
    mes = email_publish.publish(dict1)
    assert mes == 'The subject could not create as empty'
    if os.path.exists(mail):
        os.remove(mail)

def test_canot_login():
    dict1 = {'to': 'abc', 'message':'abcd','subject':'hjgsjhbs'}
    mes = email_publish.publish(dict1)
    assert mes == 'could not authenticate'
    if os.path.exists(mail):
        os.remove(mail)
