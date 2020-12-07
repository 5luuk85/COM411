class Robot:

  # Class attributes
  LAWS = "Protect, Obey and Survive"
  MAX_ENERGY = 100

  # A class method
  def the_laws():
    print(Robot.LAWS)#[1]

  # An initialiser (special instance method)
  def __init__(self,robot, age=0): #Setting default value of age parameter

    # An instance attribute
    self.name = robot
    self.age = age
    self.energy = Robot.MAX_ENERGY

########################### Added methods for Activity 3 ###########################
  def grow(self):
    self.age += 1

  def eat(self, amount):
    #If statement to ensure MAX_ENERGY is not exceeded
    if (self.energy + amount > Robot.MAX_ENERGY): 
      self.energy = Robot.MAX_ENERGY
    else:
      self.energy += amount

  def move(self, distance):
    if (self.energy - distance < 0): 
      self.energy = 0
    else:
      self.energy -= distance
########################### Added methods for Activity 3 ###########################

  # An instance method
  def display(self):
    print(f"I am {self.name}")


  def __repr__(self):
    return f"robot(name= {self.name}, age= {self.age}), energy= {self.energy}"#[2]

  def __str__(self):
    return f"My name is {self.name}, I am {self.age} years old and my energy is {self.energy}."#[3]

if (__name__ == "__main__"):
  robot = Robot()

  #robot.display()
  #Robot.the_laws()#[1]
  
  #print(robot.__repr__())#[2]
  #print(robot.__str__())#[3]
  
  ########################### Added methods for Activity 3 ###########################
  print(repr(robot))
  robot.grow()
  robot.move(30)  #Calling instance methods
  print(repr(robot))
   
  robot.eat(20)
  print(repr(robot))
  print(robot)
  #print(str(robot)) #Doesn't work
  
  ########################### Added methods for Activity 3 ###########################
  Robot.the_laws()








 
 
 
 
 
 
