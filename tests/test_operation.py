from src.math_operation import add,subtract

def test_add():
    assert add(2,3)==5
    assert add(-2,-4)==-6

def test_subtract():
    assert subtract(2,3)==-1
    assert subtract(-2,-4)==3