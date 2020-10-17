#The bridge that Beep and Bop were crossing has colapsed, we need to create a program to help them climd the bridge together.

def run():

  def climb_ladder(remaining, crossed):
    print("We have crossed", crossed,"steps and have", remaining, "remaining to climd!")
    
    #The comparrision of the values of our parameters
    if remaining > crossed:
      print("Still some way to go!")
    else:
      print("We are almost there!")

#The calling of our defined function.
#climb_ladder(3, 6)
#climb_ladder(8, 5)