#When creating new classes, a new separte file should be created for each class

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

  # An instance method
  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"): #Line to test code; the if statement
  robot = Robot()
  robot.display()
  Robot.the_laws()#[2]