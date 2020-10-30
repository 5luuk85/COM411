
def observe():

  observations = [] #Empty list

  for count in range(7):
    print("Please enter an observation:")
    user_input = input()
    observations.append(user_input)
    #".append" is readinng in the user input and saving it to the variable 

  return observations


def run():
  print("Counting observations...")

  observations = observe() #The list of user inputs called into a variable
  observation_set = set() #A set will need to created 

  #Populate set
  for observation in observations:
    occurances = observations.count(observation) #(1)
    observation_set.add((observation, occurances)) #(2)

  #(1) The ".count" will count how many times the "observation" variable is within in the list "observations". 
  #(2) The ".add" is used to add elements into the set, in this case we've added a tuple. The tuple added contains the loop variable "observation" and the count of list "occurances". Bear in mine that to add the tupples, double brackets must be used or it will not work.

  #Display set
  for objects in observation_set: #(3)
    observation = objects[0] #(4)
    count = objects [1] #(4)

    print(f"{observation} oberved {count} times.") #(5)

    #(3) The "objects" variable is the tuples within the data set "observation_set" 

    #(4) The data within the tuples will need to be assigned to a variable in order for the data to be displayed in the later print statement. "Observation" is assigned to the tuple "objects" with the data position of 1 "[0]" and "count" with the tuple "objects" position of 2 "[1]". 

    #(5) "f" string, a format string where we can add the defined variables into the curly brackets


run()

  #for key, value in observation_set:
    #print(f"{key} observed {value} times.")
  #Above is another neater way to display the outcome, instead of assigning variables to the tuples in the list within the set, the "key, value" variables within the for loop simply defualt extracts the values from the tuple.