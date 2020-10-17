#The "and" operator. The "or" operator will test if one side of the statement is true but the and operator will evalute both sides of the boolean as true.

def run():

  print("""
  What did I hear?
  """)
  hear = input()

  print("""
  What did I see?
  """)
  see = input()

  #The and operator evaluates the variables "hear" and "see" in this if statement and they are both true in this case.
  print()
  if ((hear == "grr") and (see =="two red eyes")):
    print("There is a scary creature. I should get out of here!")
  else:
    print("I am a little scared but I will continue.")
