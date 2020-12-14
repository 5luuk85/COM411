from abc import ABC, abstractmethod

class Tech(ABC):

  @abstractmethod
  def activate():
    pass
  #Method has no functionality at the moment

  @abstractmethod
  def deactivate():
    pass
  #By using an abstract method (or class), it forces a subclass to implement behavious from these methods


#Test code, shouldn't work because methods are not instantiated
#if (__name__ == "__main__"): 
  #tech = Tech()

  #tech.activate()
  #tech.deactivate()
