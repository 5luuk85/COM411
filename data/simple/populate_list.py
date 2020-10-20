#Populating a list

def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

  return directions


def menu():
  print("Please select a direction.")
  direction_option = directions()

  for index in range (0, len(direction_option), 1):
    print("{}:{}". format(index, direction_option[index]))

  user_response = int(input())

  return direction_option[user_response]
#"direction_option" is calling the list from "directions()" in the previous function. The user input is an integer and when returning the value back to the function, the user response,"[user_response]", will be an index of the list.


def run():
  route = []

  print("Working out escape route...")

  #If we want to run a loop a number of times, just enter the number of times, no need for anything else.
  for turns in range(5): 
    direction = menu() 
    route.append(direction)

    #When calling "menu()" we have to assign it to a variable, othereise it doesn't work. In this particular example, we get a direction so we've named the variable "direction" just so it makes sense to us.

    #"route.append(direction)" the append function is to populate a list. So in this case our list named "route = []" will be populated with the user inputs from "direction", which is the user input from "menu()".
    
  print("Escape route: {}". format(route))

run()