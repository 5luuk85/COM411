#Activity 5

from human_instance_methods import Human 
from robot_instance_methods import Robot
#imoprting the classes from other files to work on this one 

class Planet: #Class

  def __init__(self): #Instance method using dictionary
    self.inhabitants = { 
      'humans' : [], 
      'robots' : []
    }


  def add_human(self, human): #Methods
    self.inhabitants['humans'].append(human)

  def remove_human(self, human):
    self.inhabitants['humans'].remove(human)


  def add_robot(self, robot): #Methods
    self.inhabitants['robots'].append(robot)

  def remove_robot(self, robot):
    self.inhabitants['robots'].remove(robot)



  def __repr__(self): #Magic methods
    return f"planet(humans- {self.inhabitants['humans']}, robots- {self.inhabitants['robots']})"

  def __str__(self):
    return f"This planet has: humans- {len(self.inhabitants['humans'])} and robots- {len(self.inhabitants['robots'])}"
    


if (__name__ == "__main__"): #Used to display the methods
  planet = Planet()
  print(planet)
  print(repr(planet))

  jed = Human("Jed") #Adding a human entity to Human class
  planet.add_human(jed)

  rtx3060 = Robot("rtx3060") #Adding a robot entity to Robot class
  planet.add_robot(rtx3060)

  print(repr(planet))
  print(planet)