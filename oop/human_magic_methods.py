
class Human:

  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

    # An instance method
  def display(self):
    print(f"I am {self.name}")
    
########################### Added magic methods for Activity 2 ###########################
  def __repr__(self): #[A]
    return f'human(name= {self.name}, age= {self.age}, energy={self.energy})'#[4]

  def __str__(self): #{B}
    return f'I am {self.name} and I am {self.age} years old, my energy is {self.energy}.'#[5]
  #[A]'__repr__' magic method build into python, returns a formal string representation of the object

  #[B]'__str__' magic method build into python, returns an informal string representation of the object
########################### Added magic methods for Activity 2 ###########################

if (__name__ == "__main__"):
  human = Human()
  #human.display()
  print(human.__repr__()) #[4] Printing thestring returned from '__repr__' magic method
  print(human.__str__()) #[5] Printing thestring returned from '__str__' magic method