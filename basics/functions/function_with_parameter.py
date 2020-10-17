#Program to help beep and bop escape the cave from the boudler.
#The use of a parameter with our defined function. The parameter is in italics in the brackets next to the function, as shown below.

def run():

  def escape_by(plan):
    print("What is our escape plan?")
    print()
  #The "plan" parameter for our function is only local to this function and cannot be used in anywhere else.

  #We can set conditions and values for the "plan" parameter, in this case we used an if statement to set the string values. 
    if plan == "jumping over":
      print("We cannot escape that way! The Boulder is too big!")
      print()

    elif plan == "running around":
      print("We cannot escape tat way! The boudler is moving too fast!")
      print()
    
    elif plan == "going deeper":
      print("That might just work! Lets go deeper!")
      print()

    else:
      print("We cannot escape that way! The boulder is in the way!")

#Calling of our defined function with its set parameters in the brackets.
#escape_by("jumping over")
#escape_by("running around")
#escape_by("going deeper")
#escape_by("run towards it")