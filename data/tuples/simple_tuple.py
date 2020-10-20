#Beep and Bop have come accross falling trap steps in the cave.
#We need to help create a program to help them decide which steps to take.

#A tuple is similar to a list but the data stored within a tuple is static and cannot be changed. Tuple in example "likelihoods = (50, 38, 27, 99, 4)" 

def likelihood():
  likelihoods = (50, 38, 27, 99, 4)

  return (min(likelihoods))
  #We can return the minimum value of the tuple by the "min" fnction, the same goe with the "max" function if we want to return the maximum value.

def run():
  returned_value = likelihood()

  print("Minimum value of falling: {}%". format(returned_value))

run()