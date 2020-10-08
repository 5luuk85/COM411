print()
print("I wish to compare two numbers to find the samllest number.")
print("Please enter the first number.")
first_number = int(input())
print()

print("Please enter the second number.")
second_number = int(input())
print()

if (first_number < second_number):
  print("The first number is the smallest!")

elif (first_number > second_number):
  print("The second number is smallest!")

#We could do an first_number == second_number but, as the if and elif statements above already work out which one is smaller or bigger than the other, the only remainder to for the else statement would have to be two numbers that are the same.
else:
 print("Both numbers are equal!")