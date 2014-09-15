from channels import email_publish
import ConfigParser
import os


mail = email_publish.mail_credential
assert mail == ".credentials"

def test_if_section():
    addres = "amvarish"
    pasw = "amvarish"
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if not cfg.has_section('mail'):
        cfg.add_section('mail')
        cfg.set('mail', 'mailaddres', addres)
        cfg.set('mail', 'password', pasw)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    ab,cd = email_publish.get_value()
    assert ab == addres
    assert cd == pasw
    
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if cfg.has_section('mail'):
        cfg.remove_section('mail')
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    

def test_if_not_section():
    ab,cd = email_publish.get_value()
    ab = ab.decode('base64','strict');
    cd = cd.decode('base64','strict');

    assert ab == "amvarish"
    assert cd == "amvarish"


def test_if_file_not_exixt():
    if os.path.exists(mail):
        os.remove(mail)
    email_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    ab = cfg.get('mail', 'mailaddres')
    bc = cfg.get('mail', 'password')
    ab = ab.decode('base64','strict');
    bc = bc.decode('base64','strict');
    assert ab == "amvarish"
    assert bc == "amvarish"


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
    assert ab == "YW12YXJpc2g="
    assert bc == "YW12YXJpc2g="
    if os.path.exists(mail):
        os.remove(mail)

def test_if_option_exist_in_file():
    addres = 'YW12YXJpc2g='
    pasw = 'YW12YXJpc2g='
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if not cfg.has_section('mail'):
        cfg.add_section('mail')
        cfg.set('mail', 'mailaddres', addres)
        cfg.set('mail', 'password', pasw)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    email_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    ab = cfg.get('mail', 'mailaddres')
    bc = cfg.get('mail', 'password')
    assert ab == addres
    assert bc == pasw
    if os.path.exists(mail):
        os.remove(mail)

def object_has_created():
    addres = '3skmnksjnk'
    pasw = 'akjhskla'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if not cfg.has_section('mail'):
        cfg.add_section('mail')
        cfg.set('mail', 'mailaddres', addres)
        cfg.set('mail', 'password', pasw)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    ab = email_publish.initialise()
    cd = Client(addres,pasw)
    assert ab == cd
    if os.path.exists(mail):
        os.remove(mail)


def test_to_address():
    dict1 = {'toac': 'abc', 'message':'abcd'}
    mes = email_publish.publish(dict1)
    assert mes == 'The input in mail (to address) may be wrong. Check your input methode'
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
    assert mes == 'The input in mail (message) may be wrong. Check your input methode'
    if os.path.exists(mail):
        os.remove(mail)


def test_message_empty():
    dict1 = {'to': 'abc', 'message':'', 'subject':'hjgsjhbs'}
    mes = email_publish.publish(dict1)
    assert mes == 'could not authenticate'
    if os.path.exists(mail):
        os.remove(mail)

def test_subject():
    dict1 = {'to': 'abc', 'message':'abcd','subjbect':'abcd'}
    mes = email_publish.publish(dict1)
    assert mes == 'The input in mail (subject)may be wrong. Check your input methode'
    if os.path.exists(mail):
        os.remove(mail)


def test_subject_empty():
    dict1 = {'to': 'abc', 'message':'abcd','subject':''}
    mes = email_publish.publish(dict1)
    assert mes == 'could not authenticate'
    if os.path.exists(mail):
        os.remove(mail)

def test_canot_login():
    dict1 = {'to': 'abc', 'message':'abcd','subject':'hjgsjhbs'}
    mes = email_publish.publish(dict1)
    assert mes == 'could not authenticate'
    if os.path.exists(mail):
        os.remove(mail)
