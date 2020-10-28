
def observe():

  observations = [] #Empty list

  for user_input in range(3):
    print("Please enter an observartion:")
    user_input = input()
    observations.append(user_input)
    #".append" is readinng in the user input and saving it to the variable 

  return observations


def run():
  print("Counting observations...")

  observations = observe() #The list of user inputs called into a variable
  observation_set = set() #A set will need to created 

  for observation in observations:
    occurances = observations.count(observation) #(1)
    observation_set.add((observation, occurances)) #(2)

  #(1) The ".count" will count the occurances of an entry in the list from "observations"
  #(2) The ".add" is used to add elements into the set, in this case we've added a tuple. The tuple added contains the loop variable "observation" and the count of list "occurances". 

  print(observation_set)
    
 
run()