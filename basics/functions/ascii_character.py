#Program that will convert an ASCII code to a character. ASCII codes are between the numbers 32-126, see SOL for the table of codes and characters.

def run():

  print("Program started!")
  print("Please enter an ASCII code (a number between 32-126).")
  print()
  ASCII_code = int(input())
  print()

  #the in range functions helps to determine if the value of the user input ASII_CODE is true in the number ranges.
  if ASCII_code in range (32, 126):
    print("The character represented by the ASCII code {} ".format(ASCII_code), end="")
    print("is {}.". format(chr(ASCII_code)))
    print()
  #chr() will return a value to a suitable character when a valid ascii code is entered.

  else:
    print("Invalid input, please lease enter a number between 32-126.")