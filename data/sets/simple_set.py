#Simple set
#***Description of a set to be entered here***
#Beep and Bop have made it out of the cave and discover a robot city, we need to create a program that will help them record what they see. 

#A set can be defined by curly brackets or by "set()"

#(1) When using curly brackets to populate a set, the brackets must have some data in it otherwise it is considered an empty dictionary instead of the input data for a set.

def observe():
  observations = set()
  observations = {"Flying Car", "Sky Scraper", "Laser", "Dome"}#(1)

  return observations

def run():
  observations = observe()
  print (observations)

run()