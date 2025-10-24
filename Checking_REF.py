M = []

num_rows = int(input("Enter the number of rows your matrix: "))
num_columns = int(input("Enter the number of columns of your matrix: "))


for i in range(num_rows):
  temp_row = []
  for j in range(num_columns):
    temp_row.append(0.0)
  M.append(temp_row)

for i in range(num_rows):
  input_row = input("Input row "+ str(i) + " as a list of numbers separated by a comma: ")
  temp_row = input_row.split(",")
  for j in range(len(temp_row)):
    M[i][j] = float(temp_row[j])

prev_pivot_pos = 0
curr_pivot_pos = 0
tracker = 0

for i in range(num_rows):
  for j in range(num_columns):
    if(M[i][j]!=0):
      curr_pivot_pos = j
      break
  if(curr_pivot_pos <= prev_pivot_pos):
    tracker = 1
    break

if(tracker == 1):
  print("This matrix IS NOT in row echelon form")
else:
  print("This matrix IS in row echelon form")
