from channels import email_publish
import ConfigParser
import os
import __builtin__
import getpass

mail = email_publish.mail_credential
assert mail == ".credentials"

def test_if_section():
    addres = "hai"
    pasw = "hai"
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
    

def test_if_not_section(monkeypatch):
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    ab,cd = email_publish.get_value()
    ab = ab.decode('base64','strict');
    cd = cd.decode('base64','strict');

    assert ab == "hai"
    assert cd == "hai"


def test_if_file_not_exixt(monkeypatch):
    if os.path.exists(mail):
        os.remove(mail)
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    email_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    ab = cfg.get('mail', 'mailaddres')
    bc = cfg.get('mail', 'password')
    ab = ab.decode('base64','strict');
    bc = bc.decode('base64','strict');
    assert ab == "hai"
    assert bc == "hai"


def test_if_option_not_exixt_in_file(monkeypatch):
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if cfg.has_section('mail'):
        cfg.remove_section('mail')
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    email_publish.initialise()
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    ab = cfg.get('mail', 'mailaddres')
    bc = cfg.get('mail', 'password')
    assert ab == "aGFp"
    assert bc == "aGFp"
    if os.path.exists(mail):
        os.remove(mail)

def test_if_option_exist_in_file(monkeypatch):
    addres = 'aGFp'
    pasw = 'aGFp'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail)
    if not cfg.has_section('mail'):
        cfg.add_section('mail')
        cfg.set('mail', 'mailaddres', addres)
        cfg.set('mail', 'password', pasw)
    with open('.credentials', 'wb') as configfile:
        cfg.write(configfile)
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
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


def test_to_address(monkeypatch):
    dict1 = {'toac': 'abc', 'message':'abcd'}
    def mock_raw_input(*args, **kwargs):
        return "amvarish";
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = email_publish.publish(dict1)
    assert mes == 'The input in mail (to address) may be wrong. Check your input methode'
    if os.path.exists(mail):
        os.remove(mail)

def test_to_address_empty(monkeypatch):
    dict1 = {'to':'', 'message':'abcd'}
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = email_publish.publish(dict1)
    assert mes == 'The to address could not create as empty'
    if os.path.exists(mail):
        os.remove(mail)

def test_message(monkeypatch):
    dict1 = {'to': 'abc', 'messsage':'abcd'}
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = email_publish.publish(dict1)
    assert mes == 'The input in mail (message) may be wrong. Check your input methode'
    if os.path.exists(mail):
        os.remove(mail)


def test_message_empty(monkeypatch):
    dict1 = {'to': 'abc', 'message':'', 'subject':'hjgsjhbs'}
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = email_publish.publish(dict1)
    assert mes == 'Given option is wrong:'
    if os.path.exists(mail):
        os.remove(mail)

def test_subject(monkeypatch):
    dict1 = {'to': 'abc', 'message':'abcd','subjbect':'abcd'}
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = email_publish.publish(dict1)
    assert mes == 'The input in mail (subject)may be wrong. Check your input methode'
    if os.path.exists(mail):
        os.remove(mail)


def test_subject_empty(monkeypatch):
    dict1 = {'to': 'abc', 'message':'abcd','subject':''}
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = email_publish.publish(dict1)
    assert mes == 'Given option is wrong:'
    if os.path.exists(mail):
        os.remove(mail)

def test_canot_login(monkeypatch):
    dict1 = {'to': 'abc', 'message':'abcd','subject':'hjgsjhbs'}
    def mock_raw_input(*args, **kwargs):
        return 'hai';
    monkeypatch.setattr(__builtin__, 'raw_input', mock_raw_input)
    monkeypatch.setattr(getpass, 'getpass', mock_raw_input)
    mes = email_publish.publish(dict1)
    assert mes == 'could not authenticate'
    if os.path.exists(mail):
        os.remove(mail)
