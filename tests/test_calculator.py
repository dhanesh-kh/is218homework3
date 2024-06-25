'''My Calculator Test'''
from decimal import Decimal
import pytest
from calculator import add, subtract, multiply, divide
from calculator.calculation import Calculation

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that test_multiplication function works ''' 
    assert multiply(2,2) == 4

def test_division():
    '''Test that test_division function works '''
    assert divide(2,2) == 1

def test_divisionbyzero():
    '''Test that exception throwing works '''
    with pytest.raises(ValueError, match="divided by zero"):
        divide(1, 0)

def test_operations(a, b, operation, expected):
    assert operation(a, b) == expected

def test_operations_generated(a, b, operation, expected):
    if expected == "ZeroDivisionError":
        with pytest.raises(ValueError) as exc_info:
            operation(a, b)
        assert str(exc_info.value) == "Cannot divide by zero"
    else:
        assert operation(a, b) == expected

