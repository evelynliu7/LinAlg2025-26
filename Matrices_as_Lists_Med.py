import copy
from tabulate import tabulate

M = []
m = int(input("Choose the number of rows in your matrix: "))
n = int(input("Choose the number of columns in your matrix: "))

def AddRows(a, b, scalar):
    for i in range(n):
        M[b][i] += M[a][i]*scalar

def MultRow(a, scalar):
    for i in range(n):
        M[a][i] *= scalar

def SwapRows(a, b):
    tempRow = M[a]
    M[a] = M[b]
    M[b] = tempRow

for i in range(m):
    stringRow = input("Enter row " + str((i+1)) + ": ")
    row = list(map(int, stringRow.split()))
    M.append(row)

print("Here is the matrix:\n")
print(tabulate(M))

print("Enter 1 to multiply a row by a scalar.")
print("Enter 2 to add a scalar of one row to another row.")
print("Enter 3 to swap two rows.")
print("Enter -1 to STOP.")

action = int(input("Enter your action: "))

while(action!=-1):
    if(action == 1):
        row1 = int(input("Enter row 1: "))
        scalar = int(input("Enter the scalar you want to multiply the row by: "))
        MultRow(row1-1, scalar)

    if(action == 2):
        row1 = int(input("Enter row 1: "))
        scalar = int(input("Enter the scalar you want to multiply row 1 by: "))
        row2 = int(input("Enter row 2: "))
        AddRows(row1-1, row2-1, scalar)

    if(action == 3):
        row1 = int(input("Enter row 1: "))
        row2 = int(input("Enter row 2: "))
        SwapRows(row1-1, row2-1)

    print("Here is the current matrix:\n")
    print(tabulate(M))

    print("Enter 1 to multiply a row by a scalar.")
    print("Enter 2 to add a scalar of one row to another row.")
    print("Enter 3 to swap two rows.")
    print("Enter -1 to STOP.")

    action = int(input("Enter your action: "))