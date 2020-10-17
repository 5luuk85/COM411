#Program to determine ASCII code for a character

def run():

  print("Program started!")
  print("Please select a standard character.")
  print()
  character = str(input())
  #Input from user wis a string

  #If the length of the user input is equal to 1 is true, the below print statements will be printed below.
  if len(character) == 1:
    print("The ASCII code for {} is ".format(character), end="")
    print("{}.".format(ord(character)))
    print()
  #The ord() fetch the ascii value of the user inputs value.

  else:
    print("Please enter only one character.")


  print()
  print("Program ended!")