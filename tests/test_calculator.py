'''My Calculator Test'''
from decimal import Decimal
import pytest
from calculator import add, subtract, multiply, divide

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
    assert divide(2,0) == 0

@pytest.mark.parametrize("a, b, operation, expected_result",
[
    (Decimal('2'), Decimal('2'), add, Decimal('4')),
    (Decimal('2'), Decimal('2'), subtract, Decimal('0')),
    (Decimal('2'), Decimal('2'), multiply, Decimal('4')),
    (Decimal('2'), Decimal('2'), divide, Decimal('1')),
])
def test_operations(a, b, operation, expected_result):
    '''test operations'''
    assert operation(a, b) == expected_result
