# Put a matrix, implemented as a list of lists, into Row Echelon or Reduced Row Echelon Form
# Patrick Honner, 10/1/2022

# Need this to deepcopy lists
import copy

# We'll hardcode the matrix as a list of lists

row_1 = [3, -2, 1, 5]
row_2 = [2, -2, 3, 10]
row_3 = [7, 2, 1, 3]
M = [ row_1, row_2, row_3]


# A subroutine that converts every matrix entry to a float
def convert_matrix_entries_to_floats(M):
  for i in range(len(M)):
    for j in range(len(M[i])):
      M[i][j] = float(M[i][j])

# A subroutine that replaces any -0.0 with 0.0 in the matrix
def remove_negative_zeroes(M):
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == -0.0: M[i][j] = 0.0

      
# A function to print out a list of lists, i.e. a matrix
def print_matrix(M):
  for i in range(len(M)):
    for j in range(len(M[i])):
      print (M[i][j], "\t", end="")
    print("\n")

# A function for multiplying the row of a matrix by a scalar
# Note: This expects row-number in 0-based indexing
def multiply_row_by_scalar(M,row,scalar):
  for j in range(len(M[row])):
    M[row][j]=scalar*M[row][j]


# A function for adding a multiple of one row of a matrix to another
# Note: This expects row-number in 0-based indexing
def add_multiple_of_row_i_to_row_j(M,scalar,row_i,row_j):
  for j in range(len(M[row_j])):
    M[row_j][j]=scalar*M[row_i][j]+M[row_j][j]

# A function for swapping two rows of a matrix
# Note: This expects row-numbers in 0-based indexing
def swap_row_i_and_row_j(M,row_i,row_j):
  # First create a temporary copy of row_i
  temp_row = copy.deepcopy(M[row_j])
  
  for j in range(len(M[row_j])):
    M[row_j][j]=M[row_i][j]
    M[row_i][j]=temp_row[j]




# A subroutine that puts a matrix intro Row Echelon Form
# First makes a deep copy, then returns the copy in REF
    
def matrix_to_REF(M,skip_last_column = 0):
  N = copy.deepcopy(M)

  num_rows = len(N)
  num_columns = len(N[0])

  # Should we row-reduce the final column or not?
  if  (skip_last_column == 1): num_columns -= 1
  
  pivot_row = 0

  # Start_row tells which row to start the search for a pivot in a column
  start_row = 0

  # proceed column by column
  for j in range(num_columns):

    # Flag to indicate the we have found a pivot in a column
    pivot_found = 0

    for i in range (start_row, num_rows):
      # If we've already found a pivot in this column, zero out a non-zero entry
      if(pivot_found == 1 and N[i][j] != 0 ):
        add_multiple_of_row_i_to_row_j(N,-N[i][j],pivot_row,i)
        
      # If we haven't found a pivot in this column, look for one
      if(pivot_found == 0 and N[i][j] != 0):
        pivot_found=1

        # Make the pivot 1, swap with the "start row" for this column
        multiply_row_by_scalar(N,i,1/N[i][j])
        swap_row_i_and_row_j(N,start_row,i)

        # Set the pivot to the current start_row
        pivot_row = start_row
        # Make sure we start our search in the next column one row down
        start_row += 1

  # Removes -0.0s from the matrix. Comment this out and see what happens
  remove_negative_zeroes(N)
  
  return(N)

# A subroutine that puts a matrix intro Reduced Row Echelon Form
# First makes a deep copy, then returns the copy in REF
    
def matrix_to_RREF(M,skip_last_column = 0):
  N = copy.deepcopy(M)

  num_rows = len(N)
  num_columns = len(N[0])

  # Should we row-reduce the final column or not?
  if  (skip_last_column == 1): num_columns -= 1
  
  pivot_row = 0

  # Start_row tells which row to start the search for a pivot in a column
  start_row = 0

  # proceed column by column
  for j in range(num_columns):

    # Flag to indicate the we have found a pivot in a column
    pivot_found = 0

    # First find the pivot in a column
    for i in range (start_row, num_rows):
      
      if(N[i][j] != 0):
        # We've found a pivot
        pivot_found = 1

        # Make the pivot 1, swap with the "start row" for this column
        multiply_row_by_scalar(N,i,1/N[i][j])
        swap_row_i_and_row_j(N,start_row,i)

        # Set the pivot to the current start_row
        pivot_row = start_row

    for i in range (num_rows):
      if (i != pivot_row):
        add_multiple_of_row_i_to_row_j(N,-N[i][j],pivot_row,i)
        
    
    # Make sure we start our search for a pivot in the next column one row down
    start_row += 1

  # Removes -0.0s from the matrix. Comment this out and see what happens
  remove_negative_zeroes(N)
  
  return(N)



convert_matrix_entries_to_floats(M)

print("Original Matrix M:")
print_matrix(M)
print("\n")

print("M in Row Echelon Form")
A=matrix_to_REF(M,1)
print_matrix(A)
print("\n")

print("M in Reduced Row Echelon Form:")
B=matrix_to_RREF(M,1)
print_matrix(B)

