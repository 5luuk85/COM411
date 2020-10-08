#Counting up the amount of even and odd numbers 
print()
print("Please enter three whole numbers so that I can work out the amount of odd and even numbers.")
print()

print("Please enter the first whole number.")
first_no = int(input())
remainder_first = first_no % 2
print()

print("Please enter the second number.")
second_no = int(input())
remainder_second = second_no % 2
print()

print("Please enter the third number.")
third_no = int(input())
remainder_third = third_no % 2
print()

even_numbers = 0
odd_numbers = 0

if (remainder_first ==0):
  even_numbers = +1
else: odd_numbers = +1

if (remainder_second ==0):
  even_numbers = +1
else: odd_numbers = +1

if (remainder_third ==0):
  even_numbers = +1
else: odd_numbers = +1


print("There were {} even numbers".format (even_numbers),"and","{} odd numbers.".format(odd_numbers))