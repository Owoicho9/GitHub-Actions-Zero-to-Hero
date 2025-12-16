# app.py
# This is a test commit
def add(a, b):
    return a + b

def mut(a, b):
    return a * b
    

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def test_mut():
    assert mut(2, 1) == 2
    assert mut(3, 3) == 9
