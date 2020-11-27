import matplotlib.pyplot as plt   
import matplotlib.animation as animation
     
fig, ax = plt.subplots()
    
def animate(frame): 
  print(frame) #Prints the frame number in the terminal 
     
def run():
  global fig  

  simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)

  plt.show()

      
run()  