
import matplotlib.pyplot as plt #Plot module
import matplotlib.animation as animation #Animation module

fig, ax = plt.subplots() #Global 

def animate(frame):
  ax.set_xlim(0, 10) #Sets the limits of the axis 
  ax.set_ylim(0, 10)
  ax.plot(frame, frame, 'ro') 


def run():
  global fig
  simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  # FuncAnimation calls the animate function,in the brackets, the figure is to be animated and the amount of frames to be animated is set along with the time interval (miliseconds)
  plt.show()

run()