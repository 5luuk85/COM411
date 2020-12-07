
class Human:

  MAX_ENERGY = 100

  def __init__(self, human, age=0):
    self.name = human
    self.age = age
    self.energy = Human.MAX_ENERGY
  

########################### Added methods for Activity 3 ###########################
  def grow(self): 
    self.age += 1

  def eat(self, amount):
    #If statement to ensure MAX_ENERGY is not exceeded
    if (self.energy + amount > Human.MAX_ENERGY): 
      self.energy = Human.MAX_ENERGY
      return self.energy
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


  def __repr__(self): #[A]
    return f"human(name= {self.name}, age= {self.age}, energy={self.energy})"#[4]

  def __str__(self): #{B}
    return f"I am {self.name} and I am {self.age} years old, my energy is {self.energy}."#[5]
  #[A]'__repr__' magic method build into python, returns a formal string representation of the object

  #[B]'__str__' magic method build into python, returns an informal string representation of the object


if (__name__ == "__main__"):
  human = Human()
  #human.display()
  #human.grow()
  #print(human.__repr__()) #[4] Printing thestring returned from '__repr__' magic method
  #print(human.__str__()) #[5] Printing thestring returned from '__str__' magic method

########################### Added methods for Activity 3 ###########################
  print(repr(human))
  human.grow()
  human.move(30)  #Calling instance methods
  print(repr(human))
   
  human.eat(20)
  print(repr(human))
  print(human)
########################### Added methods for Activity 3 ###########################