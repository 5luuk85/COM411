
print("""
How many numbers should I sum up?
""")
numbers = int(input())
#User integer input
print()

summed = 0
#Control variables
total = 0

while (summed < numbers):
  total = total + numbers
  summed +=1
  print("Please enter", summed, "of", numbers, ":")
  nums = int(input())


print("The answer is", total)
