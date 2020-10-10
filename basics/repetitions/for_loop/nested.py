#Nested for loops.
print("How many rows should I have?")
rows = int(input())

print()
print("How many columns should I have?")
columns = int(input())

for number_of_rows in range (0, rows, 1):
  for number_of_columns in range(0, columns, 1):
    print (":-) " , end="")
  print()

#In this for net loop, the first statement will be the overall times the loop will be repeated, determined by the integer input from the user variable "rows". Then in the nest the local variable "number_of_columns" will be determined by the range of the user input "columns". The print statement will print following the instructions of the loop but the string ":-)" will be printed on the same line because of the "end="" " operator.