import copy
from tabulate import tabulate

def AddRows(a, b):
    print("add")

def MultRow(a, scalar):
    print("multiply")

def SwapRows(a, b):
    print("swap")


m = int(input("Choose the number of rows in your matrix: "))
n = int(input("Choose the number of columns in your matrix: "))

M = []

for i in range(m):
    row = input("Enter row " + str((i+1)) + ": ")
    M.append(list(row))

print("Here is matrix:\n")
print(tabulate(M))

print("Enter 1 to multiply a row by a scalar.")
print("Enter 2 to add a scalar of one row to another row.")
print("Enter 3 to swap two rows.")

action = int(input("Enter your action: "))

if(action == 1):
    MultRow(1, 1)
