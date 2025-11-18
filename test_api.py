from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def test_health():
    r=client.get('/health'); assert r.status_code==200 and r.json()['status']=='ok'
def test_add():
    r=client.post('/add', json={'a':2,'b':3}); assert r.status_code==200 and r.json()['result']==5
def test_get_item_found():
    r=client.get('/items/1'); assert r.status_code==200 and r.json()['name']=='pencil'
def test_get_item_not_found():
    r=client.get('/items/999'); assert r.status_code==404
