from channels import twit
import pytest
@pytest.fixture(autouse=True)
def test_twitter_publish():
    monkeypatch.delattr("requests.session.Session.request")
    data={'message':'Hello','channel':'Twitter'}
    success = twit.twitter_publish(data)
    assert success == 1
