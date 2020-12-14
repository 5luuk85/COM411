from inhabitant import Inhabitant

#Creation of subclass 'Human' using the initialiser and methods from Inhabitant parent class
class Human(Inhabitant):

  def __init__(self, name="Human", age=0):
    super().__init__(name, age)

    self.clothing = []


  def dress(self, clothing):
    self.clothing.append(clothing)

  def undress(self, clothing):
    self.clothing.remove(clothing)


  def __repr__(self):
    return f"Human(name= {self.name}, age= {self.age}, energy={self.energy})"

  def __str__(self):
    return f"I am {self.name} and I am {self.age} years old, my energy is {self.energy}."

  def display (self):
    print(f"I am {self.name} and I am {self.age} years old, my energy is {self.energy}")


if (__name__ == "__main__"):
  #create an object of type Human
  human = Human()

  #Display the current state of the object
  print(repr(human))
  
  #Invoke the method on the object
  human.move(10)

  #Display the current state of the object after move method is invoked
  print(repr(human))
  print(human)