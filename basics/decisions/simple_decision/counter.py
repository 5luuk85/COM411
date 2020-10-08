#Counting up the amount of even and odd numbers 
print()
print("Please enter three whole numbers so that I can work out the amount of odd and even numbers.")
print()

print("Please enter the first whole number.")
first_no = int(input())
print()

print("Please enter the second number.")
second_no = int(input())
print()

print("Please enter the third number.")
third_no = int(input())
print()

#The variables with a base value of 0
even_numbers = 0
odd_numbers = 0

#The if statements will take the integer inputs above do the calculations needed. If input is divided by 2 and the remainder is 0 then a value of 1 will be added to the even_numbers variable.
if (first_no % 2 ==0):
  even_numbers = even_numbers + 1
else: odd_numbers = odd_numbers + 1

#Note the odd_numbers = odd_numbers + 1, odd_numbers has to equals it self and then plus one to its saved value.

if (second_no % 2 ==0):
  even_numbers = even_numbers + 1
else: odd_numbers = odd_numbers + 1

if (third_no % 2 ==0):
  even_numbers = even_numbers + 1
else: odd_numbers = odd_numbers + 1


print("There were {} even numbers".format (even_numbers),"and","{} odd numbers.".format(odd_numbers))