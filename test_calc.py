import pytest
from calc import add, div

def test_add():
    assert add(2,3)==5

def test_div():
    assert div(6,2)==3
    with pytest.raises(ZeroDivisionError):
        div(1,0)
