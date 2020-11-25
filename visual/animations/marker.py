#Building on the simple.py example, when the animation is running through the frames, the plot is being drawn on top of the previous plot/frame essentially. To make just the one plot appear at a time and clear the previous animation, use the the ".cla()" function. The function ".cla()" means clear axis.


import matplotlib.pyplot as plt #Plot module
import matplotlib.animation as animation #Animation module

fig, ax = plt.subplots() #[1]
#Global variables, the figure and a single axes are defined for the rest of the code (in animate and run functions).

def animate(frame): #[4]
  global ax #defining the global variable for use, causes less confusion in python
  ax.cla() #[2]
  ax.set_xlim(0, 10) #[3] 
  ax.set_ylim(0, 10)
  ax.plot(frame, frame, 'ro') #[4]

#[2]".cla" means clear axes, each new frame will be drawn on a new axes so that when the  plot is bening animated or drawn, they do not overlap. In this case each marker will be drawn on the different points on the frame it is on and the previous frame/drawing is not shown while the animation is running.

#[3] Sets the limits of the axis, if not set the display of the axis will change from frame to frame during the animation, which is not ideal when trying to present data.

#[4] Notice how the the x and y axis are defined as the frame parameter in the function. The values of the x & y axis will be the same value of the frame at the time, i.e. if the animation is currently on frame 2, the values of the x and y axis will be 2. The number of frames to be run through in the animation are defined in the run function below, the values of the x and y axis in the "ax.plot" function will draw out a diaginal line due to the x and y values.

def run():
  global fig #defining the global variable for use, causes less confusion in python
  simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  # "animation.FuncAnimation" calls the animate function,in the brackets, the figure is to be animated and the amount of frames to be animated is set along with the time interval (miliseconds). When using the animate function, it has to be set to a variable to work in python, if it is run without a variable set to it, the figure will not show the animation.
  plt.show()

run()