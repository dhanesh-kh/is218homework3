from decimal import Decimal
import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import multiply


class MultiplyCommand(Command):
    
    def execute(self):
        try:
            print("Enter first number:")
            a = Decimal(input())
            print("First number:", a)
            print("Enter second number:")  
            b = Decimal(input())
            print("Second number:", b)

            calculation = Calculation(a, b, multiply)
            result = calculation.get_result()
            print("Result:", result)
            
        except (ValueError):
            print("Invalid input. Please enter valid numbers.")