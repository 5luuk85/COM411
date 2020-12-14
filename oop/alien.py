from inhabitant import Inhabitant


class Alien(Inhabitant):

  def __init__(self, name="Alien", age=0):
    super().__init__(name, age)

    self.tech = []
    

  def pickup(self, technology):
    self.tech.append(technology)

  def drop(self, technology):
    self.tech.remove(technology)


  def __repr__(self):
   return f"Alien(Name:{self.name}, Age: {self.age}, energy={self.energy}, Technology: {self.tech})"

  def __str__(self):
    return (f"I am {self.name} and my age is {self.age}. I have the {self.tech} technology.")


if (__name__ == "__main__"):
  alien = Alien()


  laser = "laser"

  alien.pickup("laser")

  print(repr(alien))
  print(alien)