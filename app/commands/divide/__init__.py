from decimal import Decimal
import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import divide


class DivideCommand(Command):
    def execute(self):
        try:
            print("Enter first number:")
            a = Decimal(input())
            print("First number:", a)
            print("Enter second number:")  
            b = Decimal(input())
            print("Second number:", b)

            calculation = Calculation(a, b, divide)
            result = calculation.get_result()
            print("Result:", result)
            
        except (ValueError):
            print("Invalid input. Please enter valid numbers.")