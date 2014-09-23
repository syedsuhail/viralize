import cli
import sys
import StringIO
import pytest

def raw_input(prompt):
    return "ssuhail"

def getpass(prompt):
    return 'Tech'



def test_get_user_data():
    data = cli.get_user_data('viral.ini')
    assert data[0]['channel'] == 'facebook'
    
    error = cli.get_user_data('hello')
    assert error == []
    
   # cli.get_user_data('viral_fail.ini')
    s = StringIO.StringIO()
    old_stdout = sys.stdout
    sys.stdout = s
  
    sys.stdout = old_stdout
    
    #with pytest.raises(Exception):
     #   cli.get_user_data('viral_fail.ini')
       # assert s.getvalue() == "In section facebook, message value is empty\n"
    
    

def test_status():
    results={'Twitter':'hellooo'}
    abc = "hellooo"
    s = StringIO.StringIO()
    old_stdout = sys.stdout
    sys.stdout = s
    cli.status(results,abc)
    sys.stdout = old_stdout
    assert s.getvalue() == "\x1b[1;32m================== hellooo =========================\x1b[1;m\nStatus :  {'Twitter': 'hellooo'}\n"
