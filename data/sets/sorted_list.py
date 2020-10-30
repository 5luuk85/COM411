

def observed():
  
  observations = []
  print("Please enter an observation:")
  for user_input in range(5):
    
    user_input = input
    observations.append(user_input)
  
  return observations

def remove_observation(list_of_observations):

  is_running = True
  
  while is_running:
    print("Do you wish to remove an observation (yes/no)")
    decision = input()

    if decision.lower == "yes":
      print("Please enter the observation you wish to remove:")
      remove = input()

      list_of_observations.remove(remove)
      print("Done!")
    
    else:
      is_running = False





def run():
  the_observations = observed() 
  removal_of_observations = remove_observation(the_observations)

  set_of_observations = set()

  for observations in set_of_observations:
    occurances = removal_of_observations.count(observations)
    set_of_observations.add ((observations, occurances))

  print("Observations:")
  print(set_of_observations)

run()