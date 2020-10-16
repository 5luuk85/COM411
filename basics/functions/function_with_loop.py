#Beep and Bop have come accross a bridge and they need to cross it one step at a time.
#Using a loop to give the parameter value in a loop

def cross_bridge(steps):

#The "in range (steps)" doesn't nessisarily need a limit number set to it, i.e. (steps < 5), the value set to the calling of the function will be counted and later we have an if statement to set some conditions for our function. 
  for steps in range (steps):
    print("Crossed step...")

  if steps > 5 :
    print("The bridge is collapsing!")

  else:
    print("We must keep going!")
  
#The callings of our function  
#cross_bridge(1)
#cross_bridge(2)
#cross_bridge(3)
#cross_bridge(4)
#cross_bridge(5)
#cross_bridge(6)
#cross_bridge(7)