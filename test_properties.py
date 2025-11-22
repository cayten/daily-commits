from hypothesis import given, strategies as st
from mathops import rev, assoc_add

@given(st.text())
def test_reverse_involution(s):
    assert rev(rev(s))==s

@given(st.integers(), st.integers(), st.integers())
def test_add_assoc(a,b,c):
    l,r=assoc_add(a,b,c)
    assert l==r
