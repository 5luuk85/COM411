import matplotlib.pyplot as plt   
import matplotlib.animation as animation
     
fig, ax = plt.subplots()
    
def animate(frame): 
  print(int(frame))
     
def run():
  global fig  

  animation.FuncAnimation(fig, animate, frames = 10, interval = 10000)

  plt.show()

#The function should create an animation using FuncAnimation which calls the function animate, has 10 frames and an interval of 1000 milliseconds.
#Finally, the function should show the plot.

      
run()  