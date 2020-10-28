

def observed():
  
  observations = []
  
  for user_input in range(5):
    print("Please enter an observation:")
    user_input = input
    observations.append(user_input)
  
  return observations

def remove_observation(list_of_observations):
  print("Do you wish to remove an observation (yes/no)?")
  decision = input() 

  list_of_observations = observed()

  while decision == "yes":
    print("Please enter the observation you whish to remove:")
    remove = input()
    print("Done!")
    list_of_observations.remove(remove)


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