def observe():
  print("Counting observations...")
  observations = []

  for user_input in range(7):
    print("Please enter an observartion...")
    user_input = input()
    observations.append(user_input)

  return observations


def run():
  #print("Counting observations...")

  observations = observe()
  observation_set = set()
  for observation in observations:
    observation_set.add((observation, observations.count(observation)))

  print(observation_set)
    
 
run()
