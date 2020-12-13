from inhabitant import Inhabitant

#Creation of subclass 'Robot' using the initialiser and methods from Inhabitant parent class

class Robot(Inhabitant):

  #Class attribute
  LAWS = "Protect, Obey and Survive" 

  def __init__(self):
    super().__init__()

  def the_laws(): #Static class method for Robot class
    print(Robot.LAWS)
  
  def __repr__(self):
    return f"Robot(name= {self.name}, age= {self.age}, energy={self.energy})"

  def __str__(self):
    return f"I am {self.name} and I am {self.age} years old, my energy is {self.energy}."

  def display (self):
    print(f"I am {self.name} and I am {self.age} years old, my energy is {self.energy}")


if (__name__ == "__main__"):
  #create an object of type Robot
  robot = Robot()

  #Display the current state of the object
  print(repr(robot))
  
  #Invoke the method on the object
  robot.move(10)

  #Display the current state of the object after move method is invoked
  print(repr(robot))
  print(robot)
  Robot.the_laws()


