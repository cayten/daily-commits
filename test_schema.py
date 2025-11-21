import json, pathlib
from jsonschema import validate, ValidationError

BASE = pathlib.Path(__file__).resolve().parents[1]
SCHEMA=json.load(open(BASE/'schema'/'order.schema.json','r',encoding='utf-8'))
def test_ok():
    data=json.load(open(BASE/'samples'/'order_ok.json','r',encoding='utf-8'))
    validate(data, SCHEMA)
def test_bad():
    data=json.load(open(BASE/'samples'/'order_bad.json','r',encoding='utf-8'))
    try:
        validate(data, SCHEMA)
        assert False
    except ValidationError:
        pass
