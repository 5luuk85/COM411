

import matplotlib.pyplot as plt

def combined():
  
  redx = [3, 5, 7, 3]
  redy = [3, 5, 3, 3]
  
  plt.plot(redx, redy, 'r--o')
  
  bluex = [5, 3, 7, 5]
  bluey = [3, 5, 5, 3]
    
  plt.plot(bluex, bluey, 'b:s')
    
  greenx = [3, 3, 7, 3]
  greeny = [3, 5, 4, 3]
    
  plt.plot(greenx, greeny, 'g-.*')
    
  yellowx = [7, 7, 3, 7]
  yellowy = [3, 5, 4, 3]
    
  plt.plot(yellowx, yellowy, 'g-.*')
    
  plt.show()
    
    
combined()