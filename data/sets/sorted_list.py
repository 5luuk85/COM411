

def observed():
  
  observations = []
  
  for user_input in range(5):
    print("Please enter an observation:")
    user_input = input()
    observations.append(user_input)
    print()
 
  return observations

def remove_observation(list_of_observations): 
  #The parameter "list_of_observations" for the function represnts the list in this case, the parameter will be populated with data in a later function.

  loop_is_running = True #Control variable for the while loop, it sets the condition as true.
  
  while loop_is_running: #The while loop is runnong on the true condition set by the "is_running" variable.

    print("Do you wish to remove an observation (yes/no)")
    decision = input()
    print()

    if decision == "yes":
      print("Please enter the observation you wish to remove:")
      remove = input()

      list_of_observations.remove(remove) #(1)
      print("Done!")
      print()
    
    else:
      loop_is_running = False #(2)

#(1) ".remove" will remove an element from the list, in this case it is removing the user input from the variable "remove". 
#(2) The "loop_is_running" control variable will change to False to stop the loop from running is the condition in the if statement is not met.



def run():
  observations = observed() #Call first function
  remove_observation(observations) #Call seconond function with parameter set to data from first funtion

  observations_sets = set() #Created an empty set to be populated

  for observation in observations: #for loop with control variable and the list "observations"
    occurances = observations.count(observation) #(3)
    observations_sets.add((observation, occurances)) #(4)

  #(3) The "occurances" variable will count the amount times the "observation" control variable within the for loop is within the list "(observation)", in other words it counts the amount of entries in the list. 
  #(4) The tupple of the entries "observation" and the count of entries "occurances" is added to the set "observations_sets" using the ".add" function. The tuples added must be in double round brackets in order for it to work.nonlocal

  for observation, times_observed in sorted(observations_sets):#(5a, 5b)
    print(f"{observation} observed {times_observed} times.")

  #(5a) The "sorted" function will often sort the given data, in this case the "(observations_sets), into an order such as alphabetical. 
  
  #(5b) The short-hand way to write out the for loop for an "f" or format string. It defualt picks out the key and value of the tuples within the set. The key in this case is the "observation" variable and the value is the "times_observed" variable within the for loop. When using this method, just remember that the first variable is always the key and the second is the value. Tuple structure --> (Key, Value)

run()

  #for count in sorted(observations_sets):
    #observation = count [0]
    #times_observed = count [1]
  #The way to display the key and value if they are defined by variables, but this was is often longer to write out.