from unittest.mock import Mock
from service import Service

def test_found():
    repo=Mock(); repo.get_user.return_value={'id':1,'name':'CAYTEN'}
    svc=Service(repo)
    assert svc.welcome(1)=='hello CAYTEN'
def test_not_found():
    repo=Mock(); repo.get_user.return_value=None
    svc=Service(repo)
    assert svc.welcome(42)=='not found'
