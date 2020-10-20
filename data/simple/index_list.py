#Beep and Bop devise a plan to escape the maze. 
#We need to create a variation of the previous simple_list program to help them escape. 

def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]

  return path

  #The list, stored in the brackets [], contains a total of 8 stored objects. A list can stored multiple types of objects, in this case strings and integers are stored. 
  
  #The objects are also ordered from left to right, each object with a position on the list, "Moving forward" has a position of 0 and the integer 1 has a position of 7. The positions of of the list start from 0.
  

def run():
  print("moving...")
  path = movements()

  #The in range function will start from the position 0, read in the number of entries in the list of "path" from the "len" function and go up in increments of 2 at a time, up the positions of the list. the. The reason for going up 2 at a time is because in our print statement, we are printing two positions of the list at a time.
  
  for index in range (0, len(path), 2):
    print ("{} for {} steps".format(path[index], path[index+1])) #[index+1] is plus 1 in the position of the first index, remember the positions of the objects in the list


run()

  #To print our statement, we could have used a lot of print statements but, when it gets repetitive, it's best to use a loop for cleaner code and to save effort.

  #print("{} for {}".format(path[0], path[1]))
  #print("{} for {}".format(path[2], path[3]))
  #print("{} for {}".format(path[4], path[5]))
  #print("{} for {}".format(path[6], path[7]))


  #The variable "path" with the brackets [], the numbers in the brackets are in collaboration to the position of the object within the list in the function "ovements()". The list in this case contains a total of 8 positions, starting from 0 ending at position 7.

