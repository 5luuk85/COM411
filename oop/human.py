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

  # An instance method
  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  Robot.the_laws()#[2]



class Human:

  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self):
    print(f"I am {self.name}, my energy is {self.energy}.")

if (__name__ == "__main__"):
  human = Human()
  human.display()






