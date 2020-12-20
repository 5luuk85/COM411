import random as rnd #Importing random module

from human import Human #Importing classes
from robot import Robot
from planet import Planet

class Universe:

  def __init__(self):
    self.planets = []

  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f"The Universe contains {len(self.planets)} planets."


  def generate(self):
    #Creates a new planet
    planet = Planet()

    for index in range(rnd.randint(1, 10)):
      robot = Robot(f"Robot{index}")
      planet.add_robot(robot) 

    for index in range(rnd.randint(1, 10)):
      human = Human(f"Robot{index}")
      planet.add_human(human) 

    #Populates the list of planets
    self.planets.append(planet)
   


if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  print(repr(universe))
  print(universe)
  