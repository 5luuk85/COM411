
import numpy as np #numpy module
import matplotlib.pyplot as plt #Plot module
import matplotlib.animation as animation #Animation module

#Code adapted from API document, take a look if needed: https://matplotlib.org/gallery/animation/simple_anim.html#sphx-glr-gallery-animation-simple-anim-py


fig, ax = plt.subplots() #Global variables

def animate(frame_no):
  global ax #Defining global variable 
  ax.cla() #Clear axes, for no overlapping displays

  ax.set_xlim(0, 2*np.pi) #x axis limit defined, converted to radians by "*np.pi"
  ax.set_ylim(-1, 1) #y axis limit defined, range -1 to 1 is showing oscillation

  x = np.arange(0, 2*np.pi, 0.01) #[1] Converts x values into radians
  y = np.sin(x + frame_no / 50) #[2] y values of the sine wave

  ax.plot(x, y) #plots the graph into figure 

  #[1] Values of x is in the range 0-2 in radians and goes up by 0.001. Increments of 0.01 and converting to radians is possible due to numpy funcyion "np.arange". 

  #[2] y values of the sine wave. the numpy function "np.sin" is defining y to be a sine wave using the values of x, the frame number divided by 50 "np.sin(x + frame_no / 50)". The "np.sin(x" is creating the sine wave and the "+ frame_no / 50)" is shifting the sine wave, so when animated the sine wave will be shift from 50->100->150 ect, as in how far to shift. 
 
def run():
  global fig #Defining global variable
  shift_sine_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)

  plt.show() 

run()