from tech import Tech 

class Laser(Tech):

  #Class attribute
  MAX_RANGE = 250


  #The activate and deactivate methods from the inherited abstract Tech class need to be defined in this class
  def activate(self): 
    print(f"Laser Activated")


  def fire(self, laser_range = 0): #Method with if statement to determine behaviour 
    if (laser_range > Laser.MAX_RANGE):
      print(f"Laser unable to fire at range {laser_range}... out of ranged.")
    else:
      print(f"Laser zeroed in at range {laser_range}... firing...")


  def deactivate(self):
    print(f"Laser Deactivated")




if (__name__ == "__main__"): #Test code
  laser = Laser()

  laser.activate()
  laser.fire(150)
  laser.fire(300)
  laser.deactivate()