from typing import List
import numpy as np
import Units
import sympy as sp
    

class Number:
    def __init__(self, value: str, unit: str):
        self.value = float(value)
        self.sigfigs = 0
        
        if value[-1] == ".":
            self.sigfigs = len(value) - 1
            return
        zeroCountPreDecimal = 0
        preDecimal = True
        for char in value:
            if char == ".":
                preDecimal = False
                self.sigfigs += zeroCountPreDecimal
            elif char == "0" and preDecimal:
                zeroCountPreDecimal += 1
            else:
                self.sigfigs += 1
            
            
    
    def getSigFigs(self) -> int:
        return self.sigfigs

def mean(a: List[int | float]) -> float:
    total = 0
    for item in a:
        total += item
    avg = total / len(a)
    return avg



def stdev(a: List[int | float]) -> float:
    global sigfigs
    # Calculate Standard Deviation with numpy
    result = np.std(a, ddof=1)
    return float(str(result))
    
def percentUncertainty(a: List[int | float]) -> float:
    # Calculate Percent Uncertainty with numpy
    result = np.std(a, ddof=1) / np.mean(a) * 100
    return float(str(result))
    
def printMenu():
    print("Please choose a function from the following:")    
    print("\t [1]: Mean")    
    print("\t [2]: Standard Deviation")    
    print("\t [3]: Calculate Uncertainty")    
    print("\t [n]: New Data Set")    
    print("\t [q]: Exit")    
    return input("?> ").lower()


if __name__ == "__main__":
    global sigfigs
    while True:
        choice = "0"
        