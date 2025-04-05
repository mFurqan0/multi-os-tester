import pytest
from src.math_ops import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)