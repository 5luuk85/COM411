


import matplotlib.pyplot as plt #Plot module
import matplotlib.animation as animation #Animation module
import numpy as np #[1] numpy module 
#[1] The numpy module is useful for coding to solve problems that involve mathamatical elemeents such as linear, alegra, trigonometry ect. Essentially, if the module isn't used, code relating to mathamatical solutions can be long and complicated as more loops and functions will have to be used to achieve the desired outcome.

#This example uses arrays, arrays are mathamaical data structurs like a list but an array contains different data types such as integers and floats ect.

fig, ax = plt.subplots() #Global variables for figure and axes.

def animate(frame):
  global ax #Defining the global variable used
  ax.set_xlim(0, 720) #Setting limits to axis, in this case the angle degrees, 0-720 degrees
  ax.set_ylim(-1, 1) #Representing the oscillation between -1 and 1

  x = np.arange(0, frame) #[2] numpy range array of 0 to number of frames
  x_in_radians = x * (np.pi/180) #[3] Radians, the unit measurment of degrees. 
  y = np.sin(x_in_radians) #[4] sin function in numpy

  ax.plot(x, y, 'g')

  #[2] The numpy range array (np.arange). By using a numpy range array as opposed to a normal range, i.e range(0-10), is that with the numpy range array, it also generates floats such as 0.2, 0.3 ect. Also the main benefit of using the numpy range array in this example is that, when performing an operation using a range of numbers to create a list of values, the list of values will have to be iterated through with another function such as a loop. But using an numpy array, all the numbers in the array can simply be multiplied by another value all at once without the need of another function. e.g. (not related to example) x_values =np.arange(0,100) -> doubled = x_values * 2. 

  #[3] Converting the values of x into radians, as x is currently in degrees. To convert from degrees to radians *number* X pi divided 180. The numpy module enables the mathamatic function (np.pi/180). np.pi also gets the value of PI

  #[4] The numpy sin (np.sin) function calculates the y value using the x values representing the degrees in radians


def run():
  global fig
  sine_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  #Calling animation function (animation.FuncAnimation) and defining that the figure is to be animated with the limit of frames of 720 and each frame to be displayed at intervals of 0.1 seconds (100 miliseconds). Function is assigned to a variable (sine_animation), the function has to be assigned to a variable to work in python. 

  plt.show() #show plot, don't forget to include brackets for the figure to actually show.

run()