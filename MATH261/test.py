from typing import List

def Determinant(data: List[List[float]] | List[List[int]]):
    
    col_size = len(data)
    row_size = len(data[0])
    if col_size != row_size:
        raise ValueError("Matrix must be square")
    
    if col_size == 1:
        return data[0][0]
    elif col_size == 2:
        return data[0][0] * data[1][1] - data[0][1] * data[1][0]
    else:
        determinant_total = 0
        #Prepare the submatrix
        for i in range(col_size):
            submatrix = []
            for j in range(1, col_size):
                row = []
                for k in range(col_size):
                    if k != i:
                        row.append(data[j][k])
                submatrix.append(row)
            print(submatrix)
            determinant_total += data[0][i] * (-1)**i * Determinant(submatrix)
            print(determinant_total)
            print()
rowNum = 0
inputStr = input(f"Enter data for {rowNum}: ")
matrixTest = []
while inputStr != "":
    matrixTest.append([float(x) for x in inputStr.split(" ")])
    rowNum += 1
    inputStr = input(f"Enter data for {rowNum}: ")

Determinant(matrixTest)

        
        