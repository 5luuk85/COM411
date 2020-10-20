#Beep and Bop devise a plan to escape the maze. 
#We need to create a variation of the previous simple_list program to help them escape. 

def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  
  return path

def run():
  print("moving...")

  directions = movements()
  for index in range (0, len(directions), 2):
    print("{} for {}".format (index, directions[index]))


run()