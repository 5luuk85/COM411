from abc import ABC #abc = Abstract based class

#An abstract class is where we it doesn't allow the an object to be created with the class but sub-classes can be created with the abstract class. For example: the Inhabitant class cannot be used to create an object directly but sub-classes like Human or Robot can inherit the Abstract class to create a sub-class.

class Inhabitant(ABC):

  MAX_ENERGY = 100

  #Initialialiser 
  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
  
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY

  #Methods
  def eat(self, amount):
    #If statement to ensure MAX_ENERGY is not exceeded
    if (self.energy + amount > Inhabitant.MAX_ENERGY): 
      self.energy = Inhabitant.MAX_ENERGY
      return self.energy
    else:
      self.energy += amount
  

  def grow(self): 
    self.age += 1


  def move(self, distance):
    if (self.energy - distance < 0): 
      self.energy = 0
    else:
      self.energy -= distance


  #Strings, magic methods
  def __repr__(self): 
    return f"Inhabitant(name= {self.name}, age= {self.age}, energy={self.energy})"

  def __str__(self):
    return f"I am {self.name} and I am {self.age} years old, my energy is {self.energy}."


