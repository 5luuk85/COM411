#Activity 2
from human_subclass import Human
from robot_subclass import Robot

#imoprting the classes from other files to work on this one 

class Planet: #Class

  def __init__(self): #Instance method using dictionary
    self.inhabitants = []


  def add(self, inhabitant): #Methods
    self.inhabitants.append(inhabitant)

  def remove(self, inhabitant):
    self.inhabitants.remove(inhabitant)




  def __repr__(self): #Magic methods
    return f"planet(inhabitants- {self.inhabitants})"

  def __str__(self):
    return f"This planet has {len(self.inhabitants)} inhabitants."
    


if (__name__ == "__main__"): #Used to display the methods
  planet = Planet()
  print(repr(planet))

  jed = Human("Jed") #Adding a human entity to Human class
  planet.add(jed)

  rtx3060 = Robot("rtx3060") #Adding a robot entity to Robot class
  planet.add(rtx3060)

  print(repr(planet))
  print(planet)


  num_humans = 0
  num_robots = 0

  for inhabitant in planet.inhabitants:
    if isinstance(inhabitant, Human):
      num_humans +=1
    
    else:
      num_robots +=1

  print(f"Found {num_humans} humans.")
  print(f"Found {num_robots} robots.")