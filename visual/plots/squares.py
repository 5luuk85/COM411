#The plot function can also display different outputs for the graph such as plotting the points as dots or squares for example. The line can also be changed to a dashed, dotted or solid line.
#More than one plot can be place on a graph, this essentially creates a graph with more than one layer of data

import matplotlib.pyplot as plt #imports plotting library for python 

def small():
  x = [3,4,4,3,3]
  y = [3,3,4,4,3]

  plt.plot(x, y,'ro:') 
#when using different colour and markers, the format is colour, marker shape, line type
#In the example above the format 'ro:' for the plot is red, circle marker, dotted line 

def medium():
  x = [2,5,5,2,2]
  y = [2,2,5,5,2]

  plt.plot(x, y, 'gs--') #'gs--' green, square marker, dashed line

def large():
  x = [1,6,6,1,1]
  y = [1,1,6,6,1]

  plt.plot(x, y, 'bp-') #'bp-' blue, pentagon marker, solid line

def run():
  small()
  medium()
  large()

  plt.show() #Remember to place brackets on the .show function

run()