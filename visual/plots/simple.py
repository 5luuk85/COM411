#Simple plot
#creating a line graph using the plot function 

import matplotlib.pyplot as plt 
#matplotlib is a plotting library for python

def display(x, y):

  plt.plot(x, y) #".plots" the graph using the supplied parameters in function
  plt.show() #".show" displays the graph
  #Both of the functions above create the graph

def run():
  x_values = [1,2,3,4,5]
  y_values = [1,4,9,16,25]
  #List of x and y values to be used by the first function to plot and show a graph

  display(x_values, y_values) #calling of first function, using the lists as parameters

run()