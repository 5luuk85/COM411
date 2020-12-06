class Robot:

  # A class attribute
  LAWS = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.LAWS)#[1]

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

   #An instance method
  def display(self):
    print(f"I am {self.name}")


########################### Added magic methods for Activity 2 ###########################
  def __repr__(self): #[A]
    return f'robot(name= {self.name}, age= {self.age})'#[2]

  def __str__(self): #{B}
    return f'My name is {self.name} and I am {self.age} years old.'#[3]

  #[A]'__repr__' magic method build into python, returns a formal string representation of the object

  #[B]'__str__' magic method build into python, returns an informal string representation of the object
########################### Added magic methods for Activity 2 ###########################

if (__name__ == "__main__"):
  robot = Robot() #Calling the class

  print(robot.__repr__())#[2] Printing thestring returned from '__repr__' magic method
  print(robot.__str__())#[3] Printing thestring returned from '__str__' magic method