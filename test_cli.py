import cli

def test_get_user_data():
    data= cli.get_user_data('viral.ini')
    assert data[0]['channel']=='Facebook'
    error = cli.get_user_data('hello')
    assert error == []
    
