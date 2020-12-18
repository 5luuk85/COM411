from tech import Tech

class Jetpack(Tech):

  #The activate and deactivate methods from the inherited abstract Tech class need to be defined in this class
  def activate(self):
    print("Activated jetpack")

  def fly (self, speed=0):
    print(f"Flying at the speed: {speed}")

  def deactivate(self):
    print("Deactivating jetpack")


if (__name__ == "__main__"): #Testing code
  jetpack = Jetpack()

  jetpack.activate()
  jetpack.fly()
  jetpack.deactivate()

