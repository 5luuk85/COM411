from inhabitant import Inhabitant


class Alien(Inhabitant):

  def __init__(self, name="Alien", age=0):
    super().__init__(name, age)

<<<<<<< HEAD
    self.tech = []
    
=======
  def technology(self):
    self.tech = []
>>>>>>> 27f866ec172cf174d1947d0d04ff34ea657be0b1

  def pickup(self, technology):
    self.tech.append(technology)

  def drop(self, technology):
    self.tech.remove(technology)


  def __repr__(self):
<<<<<<< HEAD
   return f"Alien(Name:{self.name}, Age: {self.age}, energy={self.energy}, Technology: {self.tech})"

  def __str__(self):
    return (f"I am {self.name} and my age is {self.age}. I have the {self.tech} technology.")


if (__name__ == "__main__"):
  alien = Alien()


  laser = "laser"

  alien.pickup("laser")

  print(repr(alien))
=======
   return f"Alien(Name:{self.name}, Age: {self.age}, Technology: {self.tech})"

  def __str__(self):
    print (f"I am {self.name} and my age is {self.age}. I have the {self.tech} technology.")


if (__name__ == "__main__"):
  alien = Alien

  print(repr(alien))

>>>>>>> 27f866ec172cf174d1947d0d04ff34ea657be0b1
  print(alien)