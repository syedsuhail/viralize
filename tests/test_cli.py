import cli
import sys
import StringIO
from binascii import hexlify
import pytest

def raw_input(prompt):
    return "ssuhail"

def getpass(prompt):
    return 'Tech'



def test_get_user_data():
    data= cli.get_user_data('viral.ini')
    assert data[0]['channel']=='facebook'
    
    error = cli.get_user_data('hello')
    assert error == []
    
   # cli.get_user_data('viral_fail.ini')
    s = StringIO.StringIO()
    old_stdout = sys.stdout
    sys.stdout = s
  
    sys.stdout = old_stdout
    
    with pytest.raises(Exception):
        cli.get_user_data('viral_fail.ini')
       # assert s.getvalue() == "In section facebook, message value is empty\n"
    
    

def test_status():
    results={'Twitter':'Hi'}
    s = StringIO.StringIO()
    old_stdout = sys.stdout
    sys.stdout = s
    cli.status(results)
    sys.stdout = old_stdout
    assert s.getvalue() == "Twitter Hi\n"

def test_get_username_pass():
    service='abc'
    cli.raw_input=raw_input
    cli.getpass = getpass
    username,password=cli.get_username_pass('hello')       
    assert username == hexlify("ssuhail")
    assert password == hexlify('Tech')
