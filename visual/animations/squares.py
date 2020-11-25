import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np


fig, ax = plt.subplots()

boxes = []

def init(): 

  boxes.append({'x':[3, 3, 4, 4, 3], 'y':[3, 4, 4, 3, 3]}) #dictionaries
  boxes.append({'x':[2, 2, 5, 5, 2], 'y':[2, 5, 5, 2, 2]})
  boxes.append({'x':[1, 1, 6, 6, 1], 'y':[1, 6, 6, 1, 1]})



def animate(frame_no):
  global ax #Defining global variable used 
  index = frame_no % len(boxes)
  ax.cla()
  ax.set_xlim(0, 7)
  ax.set_ylim(0, 7)

  ax.plot(boxes[index]['x'], boxes[index]['y'])


def run():
  global fig #Defining global variable used 

  square_plots = animation.FuncAnimation(fig, animate, frames = 100, interval = 100, init_func = init)

  plt.show()

run()