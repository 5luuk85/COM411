

def observed():
  
  observations = []
  
  for user_input in range(5):
    print("Please enter an observation:")
    user_input = input()
    observations.append(user_input)
  
  return observations

def remove_observation(list_of_observations): 
  #The parameter "list_of_observations" for the function represnts the list in this case, the parameter will be populated with data in a later function.

  loop_is_running = True #Control variable for the while loop, it sets the condition as true.
  
  while loop_is_running: #The while loop is runnong on the true condition set by the "is_running" variable.

    print("Do you wish to remove an observation (yes/no)")
    decision = input()

    if decision == "yes":
      print("Please enter the observation you wish to remove:")
      remove = input()

      list_of_observations.remove(remove) #(1)
      print("Done!")
    
    else:
      loop_is_running = False #(2)

#(1) ".remove" will remove an element from the list, in this case it is removing the user input from the variable "remove". 
#(2) The "loop_is_running" control variable will change to False to stop the loop from running is the condition in the if statement is not met.



def run():
  observations = observed() #Call first function
  remove_observation(observations) #Call seconond function with parameter set to data from first funtion

  observations_sets = set()

  for observation in observations:
    occurances = observations.count(observation)
    observations_sets.add((observation, occurances))




  for count in sorted(observations_sets):
    observation = count [0]
    times_observed = count [1]

    print(f"{observation} observed {times_observed} times.")

run()