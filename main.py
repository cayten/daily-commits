from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI(title='QA Demo API')

class Add(BaseModel):
    a: float
    b: float

items={1:{'name':'pencil','price':3.5},2:{'name':'notebook','price':12}}

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/add')
def add(req: Add):
    return {'result': req.a+req.b}

@app.get('/items/{item_id}')
def get_item(item_id:int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='not found')
    return items[item_id]
