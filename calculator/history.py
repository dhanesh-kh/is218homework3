from typing import List
from calculator.calculation import Calculation

class CalcHistory: 
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history