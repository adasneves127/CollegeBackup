import math

class eqParts:
    def __init__(self, eq: str) -> None:
        self.eq = eq
        self.parts = []
        self.operators = []
        self.numbers = []

class Equation:
    def __init__(self, eq: str) -> None:
        self.eq = eq