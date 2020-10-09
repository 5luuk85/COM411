
print("""
How many numbers should I sum up?
""")
numbers = int(input())
#User integer input
print()

summed = 0
#Control variables
total = 0

<<<<<<< HEAD
#If the variable "summed" is less than the input variable "numbers" then the following while statement should run until the amount of times the "summed" control variable reache the same value of the "numbers" input variable.
while (summed < numbers):
  summed +=1
  print("Please enter", summed, "of", numbers, ":")
  nums = int(input())
  total = total + nums

=======
while (summed < numbers):
  total = total + numbers
  summed +=1
  print("Please enter", summed, "of", numbers, ":")
  nums = int(input())
>>>>>>> f9dfa98816f860b3c9d8a00235f81185d3826079


print("The answer is", total)
