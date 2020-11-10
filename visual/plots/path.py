
import matplotlib.pyplot as plt 


def coordinate():
  x = int(input("Please enter a X value.\n"))
  y = int(input("Please enter a Y value.\n"))

  x_and_y_values = (x, y) #Creates tuple from the input data variables x and y

  return x_and_y_values #returning a tuple to function

def path():
  print("Retrieving path...")
  x_values =[]
  y_values =[]

  for data in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])

  return x_values, y_values

def run():
  values = path()
  plt.plot (values[0], values[1], 'ro--') #values [0] is the x value from the returned list and values [1] is the y value returned from the list
  plt.show()

run()