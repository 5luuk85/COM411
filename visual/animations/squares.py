import matplotlib.pyplot as plt #Importing modules to be used 
import matplotlib.animation as animation



fig, ax = plt.subplots() #global figure and axes.

boxes = [] #Empty list, which will be populated with dictionaries from init function.

def init(): #The function that contains the data (dictionaries) for plot

  boxes.append({'x':[3, 3, 4, 4, 3], 'y':[3, 4, 4, 3, 3]}) #Small
  boxes.append({'x':[2, 2, 5, 5, 2], 'y':[2, 5, 5, 2, 2]}) #Medium
  boxes.append({'x':[1, 1, 6, 6, 1], 'y':[1, 6, 6, 1, 1]}) #Large
  #Dictionaries for the x and y axis of squares



def animate(frame_no):
  global ax #Defining global variable used 
  index = frame_no % len(boxes)#[1] Works out which bit of data to use in which frame

  ax.cla() #Clears figure to draw one square at a time, to prevent overlapping plots
  ax.set_xlim(0, 7) 
  ax.set_ylim(0, 7) #Limits of axis set to the min and maxes of x & y co-ords of squares

  ax.plot(boxes[index]['x'], boxes[index]['y'])#[2] Plotting x & y values with dictionaries

  #[1] Using the modulus operator, %, the frame number (frame_no) and the amount of items in the global list "len(boxes)", an index of which item on the list of diectionaries (boxes) is given to work out which bit of data in the list is to be used with which frame. As they're is 3 items in the list, the first frame will be the value of the first small square dictionary, second frame; the medium square dictionary and third frame; large square dictionary. The frames and the indexes will go from 0->1->2. 

  #[2] "boxes" is the list containing the dictionaries, [index] represents which dictionary is to be used be used, relative to the frame_no (see [1]), ['x'] and ['y'] are the keys for the dictionaries for the co-ords for the axis. 

def run():
  global fig #Defining global variable used 

  square_plots = animation.FuncAnimation(fig, animate, frames = 100, interval = 100, init_func = init) 
  #"init_func = init" variable calls the init function to populate the plot with data

  plt.show()

run()