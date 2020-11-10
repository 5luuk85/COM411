

import matplotlib.pyplot as plt #importing the plotting module
import random as rnd #importing random number module

def data():
  paths = {}
  
  print("What type of line would you like to use for the plot (:, -- or -) ?")
  line_style = input()

  print("What colour would you like to use for the plot (r,g or b)?")
  colour = input()

  print("What style of marker would you like to use for the plot (o, s or ^) ?")
  marker_style = input() 

  paths ['line_style'] = line_style #adding to the empty dictionary
  paths ['colour'] = colour 
  paths ['marker_style'] = marker_style
  #format for adding to a dictionary: *dictionary* [key] = *value*

  return paths


def generate():
  print("How many lines would you like to display?")
  no_of_lines = int(input())

  for lines in range(no_of_lines):#Using the integer input to determine the for loop condition 
    values = data() 
    print()
    x = rnd.randint(1, 10) #Using the imported math.randdom module
    y = rnd.randint(1, 10) #Range of random numbers set range from 1 - 10

    #Using data from dictionary, the format is shown below 
    plot_format = f"{values['colour']}{values['marker_style']}{values['line_style']}"

    plt.plot(x, y, plot_format) 


  plt.show()


def run():
  print("Running...")
  generate() 
  print("Done!")

run()
#Link so site displaying format options and what character is used to input them for a plot
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot