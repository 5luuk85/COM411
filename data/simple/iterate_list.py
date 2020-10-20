#Using a loop to create iterations of the information based on the index in the list.
#Iterating a list can be helpful when repetition is needed, we don't have to type out loads of print statements.

def run():

  def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

    return directions

  def menu():
    print("Please select a direction.")
    direction_option = directions()

    for index in range (0, len(direction_option), 1):
      print("{}:{}". format(index, direction_option[index]))

  #With the created variable "direction_option" as an example, don't forget to add the brackets [] and the name of the index function used in the for loop, otherwise when the statement prints, it prints out the whole list and not the correct item we want from the list. 

  #We don't have to name the variable within the for loop "index" to get an index, it can be named anything but in this example, it's just easier to understand.

  def run():
    menu()

  #run()