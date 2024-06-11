from decimal import Decimal


class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation):
        self.a = a
        self.b = b
        self.operation = operation
    
    def get_result(self):
        return self.operation(self.a, self.b)