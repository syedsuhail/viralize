from channels import smail

def test_gmail():
    data = smail.gmail({
            'from': 'ssuhail.ahmed93@gmail.com',
            'to': 'ssuhail.ahmed93@gmail.com',
            'subject': 'Hello Lycaeum',
            'message': 'This is a test message from my application(email)',
            'channel':'Email'
            })
    assert data == 1
                      
