# Intro to Matrix Multiplication
# A starter for exploring matrix multiplication

# Import the csv module for handling data
import csv

# Makes presenting a table of data easier
from tabulate import tabulate

# The matrix M is encoded as a list of lists
# Recall that the nested lists serve as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1.2, 3]

M = [ row_1, row_2, row_3]

# We'll import the matrix N from a file using the CSV library
# Recall: This reads in the comma separated-values as a list of lists of strings
#                                               Each line is a list

with open("matrix.txt") as f:
  reader = csv.reader(f)
  N = list(reader)

# By default lists have strings as entries, so convert them to floats
for i in range(len(N)):
  for j in range(len (N[i])):
    N[i][j]=float(N[i][j])
    

print(tabulate(M))
print("\n")
print(tabulate(N))
print("\n")


# Challenge 1
# Write a function that returns the dimensions of a matrix


# Returns the dimensions of matrix A as a tuple (number of rows, number of columns)
def matrix_dimensions(A):
  num_rows = A.len()
  num_cols = A[0].len()
  return((num_rows,num_cols))


# Challenge 2
# Write a function that determines if two matrices can be multiplied

# Returns True or False
def can_multiply_matrices(A,B):
  A_rows, A_cols = matrix_dimensions(A);
  B_rows, B_cols = matrix_dimensions(B);

  if (A_cols == B_rows):
    return True
  else:
    return False

# Challenge 3
# Write a function that determines the entry in row i, column j of the matrix product A*B 

# Returns the entry in row i, column j of the matrix product A*B

def matrix_product_entry(A,B,i,j):
  if(!can_multiply_matrices(A,B)){
    return "Cannot multiply these matrices."
  }
  else{
    # j = the col of B
    # i = the row of A

    answer = 0

    for k in range(0, B.len()):
      answer = answer + (B[k][j] * A[i][k])
    
    return answer
  }
  # Should probably check first to see if the matrices can be multiplied!
  # return 0


# Challenge 4
# Write a function that multiplies two matrices A and B

# Returns the matrix product

def matrix_product(A,B)

  # Should probably check first to see if the matrices can be multiplied!
  A_rows, A_cols = matrix_dimensions(A);
  B_rows, B_cols = matrix_dimensions(B);

  P = [[0]*A_rows]*B_cols

  if(!can_multiply_matrices(A,B)):
    return("Cannot multiply these matrices.")
  else:
    for i in range(A_rows):
      for j in range(B_cols):
        P[i][j] = matrix_product_entry(A, B, i, j)


  # Initialize a new empty list for your row lists 
  # P = []
  # Use matrix_product_entry! 

  return P

# Challenge 5
# Write a function that transposes a matrix
  
def matrix_transpose(A):
  
  M = []
  return M

  
