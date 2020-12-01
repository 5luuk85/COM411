class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)#[1]

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  def grow(self):
    self.age += 1

  # An instance method
  def display(self):
    print(f"I am {self.name}")

  def __repr__(self):
    return f'robot(name= {self.name}, age= {self.age})'#[2]

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old.'#[3]

if (__name__ == "__main__"):
  robot = Robot()
  #robot.display()
  #Robot.the_laws()#[1]
  print(robot.__repr__())#[2]
  print(robot.__str__())#[3]



class Human:

  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def grow(self):
    self.age += 1

  #def display(self):
    #print(f"I am {self.name}, my energy is {self.energy}.")

  def __repr__(self):
    return f'human(name= {self.name}, age= {self.age}, energy={self.energy})'#[4]

  def __str__(self):
    return f'I am {self.name} and I am {self.age} years old, my energy is {self.energy}.'#[5]


if (__name__ == "__main__"):
  human = Human()
  #human.display()
  print(human.__repr__()) #[4]
  print(human.__str__()) #[5]




 
 
 
 
 
 
