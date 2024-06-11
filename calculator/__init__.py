from calculator.calculation import Calculation
from calculator.history import CalcHistory
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        calc = Calculation(a, b, add)
        CalcHistory.add_calculation(calc)
        return calc.get_result()
    @staticmethod
    def subtract(a,b):
        calc = Calculation(a, b, subtract)
        CalcHistory.add_calculation(calc)
        return calc.get_result()
    @staticmethod
    def multiply(a,b):
        calc = Calculation(a, b, multiply)
        CalcHistory.add_calculation(calc)
        return calc.get_result()
    @staticmethod
    def divide(a,b):
        calc = Calculation(a, b, divide)
        CalcHistory.add_calculation(calc)
        return calc.get_result()