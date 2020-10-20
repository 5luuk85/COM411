#Tuples can be nested in various ways i.e a tuple inside a tuple, tuple inside a list,a list inside a tuple. The same applie with lists.

#Beep and bop have found some clues on the steps to improve their likelyhood of escaping, we need to create a program to help them cross the steps.

def run():

  def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    #List of tuples. The tuples themselves also have indexes e.g. ("step 1", 50), the first bit of data "step 1" is in position 0, the first position while "50" is in the second position, or second index. 
    return likelihoods


  def run():
    likelihoods = steps()

    good_steps = []
    bad_steps = []

    #The reason why there is an index "[1]" is because we are after the second number in the list of tuples. The first number has a position or index of 0 and the second 1.
    #The if statement will compare the index number in position 1 to the assign term ">=50"
    for likelihood in likelihoods:
      if (likelihood[1] >= 50):
        bad_steps.append(likelihood)
      else:
        good_steps.append(likelihoods)

    print ("Good steps: {}, Bad steps: {}".format (len(good_steps), len(bad_steps)))

  #run()