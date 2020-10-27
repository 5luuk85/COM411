

def observed():
  observations = []
  for user_input in range(5):
    print("Please enter an observation:")
    user_input = input
    observations.append(user_input)
  
  return observed

def remove_observation(list_of_observations):
  print("Do you wish to remove an observation (yes/no)?")

