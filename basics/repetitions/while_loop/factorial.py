#Calculating a factorial of a number. A factorial is a number that is times by everything lower than its value.

def run():

  print("Please enter a number.")
  number = int(input())

  #Control variables
  count = 0
  total = 1


  while(count < number):
    count = count + 1
    total = total * count
  #As the loop only runs the amount of times of what the user inputs, the variable "total" has a base value of 1. The "total" will be multiplied by the "count" variable. This is repeated until the count value is equal or more then the value of the "number" variable.

  print("The factorial is", total) 