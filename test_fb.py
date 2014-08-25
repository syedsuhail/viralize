from channels import fb

def test_fb_publish():
    data = {'message':'Hello','channel':'Facebook'}
    success = fb.fb_publish(data)
    assert success == 1
