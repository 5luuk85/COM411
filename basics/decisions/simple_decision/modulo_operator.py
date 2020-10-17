#Using the modulus operator % to determine if a number is odd or even

def run():

  print("Please ender a whole number.")
  num = int(input())
  remainder = num % 2
  #If a number is divided by 2 and the remainder is 0, then the number is an even number.
  #If there are any remainders then the number is odd

  if remainder ==0:
    print(num,"is an even number!")
  else:
    print(num,"is an odd number!")