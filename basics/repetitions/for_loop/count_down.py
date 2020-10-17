#For loop to show a count down

def run():

  print("How far away are we from the cave?")
  distance =int(input())

  #The "distance" variable is the integer input from the user. "0 , -1" means that the sequence of the range will start at 0 from the value of the "distance" and then the "-1" will mean it will decend in values of ones. 
  for count in range (distance, 0 , -1):
    print(count, "steps remaining.")

  print()
  print("We have reached the cove!")