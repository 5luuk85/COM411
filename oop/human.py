#When creating new classes, a new separte file should be created for each class

class Human:

  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self):
    print(f"I am {self.name}, my energy is {self.energy}.")

if (__name__ == "__main__"): #Line to test code; the if statement
  human = Human()
  human.display()






