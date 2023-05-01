import math

class Matrix:
    def __init__(self, components: list[list[int]]):
        self.components = components
    
    def determinant(self):
        self.components
        col_size = len(self.components)
        row_size = len(self.components[0])
        if col_size != row_size:
            raise ValueError("Matrix must be square")
        
        if col_size == 1:
            return self.components[0][0]
        elif col_size == 2:
            return self.components[0][0] * self.components[1][1] - self.components[0][1] * self.components[1][0]
        else:
            determinant_total = 0
            #Prepare the submatrix
            for i in range(col_size):
                submatrix = []
                for j in range(1, col_size):
                    row = []
                    for k in range(col_size):
                        if k != i:
                            row.append(self.components[j][k])
                    submatrix.append(row)
                print(submatrix)
                determinant_total += self.components[0][i] * (-1)**i * Determinant(submatrix)
                print(determinant_total)
                print()
class Vector:
    def __init__(self, components: list):
        self.components = components

    def scale(self, scalar: float) -> 'Vector':
        if scalar is int:
            return Vector([x * scalar for x in self.components])
        else:
            return Vector([])
               
    def dot(self, other: 'Vector'):
        if len(self) == 0 or len(other) == 0:
            return 0
        else:
            return sum([x * y for x,y in zip(self.components, other.components)])
   
    def __add__(self, other):
        returnVector = Vector([0] * max([len(self), len(other)]))
        for idx, x in enumerate(zip(self.components, other.components)):
            returnVector.components[idx] = x[0] + x[1]
       
        return returnVector
   
    def __sub__(self, other):
        returnVector = Vector([0] * max([len(self), len(other)]))
        for idx, x in enumerate(zip(self.components, other.components)):
            returnVector.components[idx] = x[0] - x[1]
       
        return returnVector
   
    def magnitude(self) -> int:
        return sum([x ** 2 for x in self.components])**0.5
   
    def __getitem__(self, i):
        return self.components[i]
       
   
    def cross(self, other: 'Vector') -> 'Vector':
        


    def angle(self, other) -> float:
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))
   
    def __len__(self):
        return len(self.components)
   
    def __str__(self):
        retstr = str(len(self.components)) + " dimension vector. <"
        for idx, data in enumerate(self.components):
            retstr += str(data)
            if idx != len(self)-1:
                retstr += ", "
        retstr += ">"
        return retstr
    
    def eigen(self):
        return self.scale(1/self.magnitude())
   
def printMenu():
    print("Please Choose an Option: ")
    print("""[1] Vector Addition
[2] Vector Subtraction
[3] Vector Cross Product
[4] Vector Dot Product
[5] Scale Vector""")
   
while True:
    printMenu()
    choice = input("? ")
    vector2Components = []
    vector1Components = []
    for x in input("V1: ").split(","):
        print(x.strip())
        vector1Components.append(float(x.strip()))
    vector1 = Vector(vector1Components)
    vector2 = Vector([])
    if choice != "5":
        for x in input("V2: ").split(","):
            vector2Components.append(float(x.strip()))
        vector2 = Vector(vector2Components)
    if choice == "1":
        print(vector1 + vector2)
    elif choice == "2":
        print(vector1 - (vector2))
    elif choice == "3":
        print(vector1.cross(vector2))
    elif choice == "4":
        print(vector1.dot(vector2))
    elif choice == "5":
        scale_factor = int(input("Scale: "))
        print(vector1.scale(scale_factor))