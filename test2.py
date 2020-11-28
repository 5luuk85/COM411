import matplotlib.pyplot as plt

def separated():
  
  fig, ax = plt.subplots(2,2)


  redx = [3, 5, 7, 3]
  redy = [3, 5, 3, 3]

  bluex = [5, 3, 7, 5]
  bluey = [3, 5, 5, 3]

  greenx = [3, 3, 7, 3]
  greeny = [3, 5, 4, 3]

  yellowx = [7, 7, 3, 7]
  yellowy = [3, 5, 4, 3]



  ax[0].plot(redx, redy, 'r--o')
  ax[1].plot(bluex, bluey, 'b:s')
  ax[2].plot(greenx, greeny, 'g-.*')
  ax[3].plot(yellowx, yellowy, 'y-p')
  
  plt.tight_layout()
  plt.show()
        
separated()

