from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI(title="CAYTEN Math API")

class AddReq(BaseModel):
    a: float
    b: float

class FracReq(BaseModel):
    n: int
    d: int

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/add")
def add(req: AddReq):
    return {"result": req.a + req.b}

@app.post("/simplify")
def simplify(req: FracReq):
    g = math.gcd(req.n, req.d)
    return {"n": req.n//g, "d": req.d//g}
