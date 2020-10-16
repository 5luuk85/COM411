#Beep is busy reading his book on the broken bridge ladder while Bop is tring to get up the ladder and carry Beep at the same time. 

#The program should use multiple functions to display a ladder.

def display_ladder(steps):
  print("|   |")

  for step in range (steps):
    print ("*****")
    print ("|   |")


def create_ladder():
  print("How many steps remain?")
  steps = int(input())
  display_ladder(steps)
#Notice how the variable we created "steps" is also the same name as the parameter we have set for our deflined function "display_ladder(steps)"
#The second function will call the first function for it's use. 

#create_ladder()