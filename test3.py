import matplotlib.pyplot as plt



def data():

  #TODO: return a list of dictionaries.  
  #Each dictionary contains the x, y and format values for a triangle.
  #The list should contain 4 triangles.

  triangles = []

  triangles.append({'redx':[3, 5, 7, 3]}, {'redy': [3, 5, 3, 3]})
  triangles.append({'bluex':[5, 3, 7, 5]}, {'bluey': [3, 5, 5, 3]})
  triangles.append({'greenx':[3, 3, 7, 3]}, {'greeny': [3, 5, 4, 3]})
  triangles.append({'yellowx':[7, 7, 3, 7]}, {'yellowy': [3, 5, 4, 3]})

  return triangles


def improved_separated():
  #TODO: utilise data() to re-draw the 4 subplots of function separated.
  triangles = data()
  
  fig, ax = plt.subplots(2,2)

  for triangle in triangles:
    red_triangle = f"{triangles['redx']}{triangles['redy']}"
    blue_triangle = f"{triangles['bluex']}{triangles['bluey']}"
    green_triangle = f"{triangles['greenx']}{triangles['greeny']}"
    yellow_triangle = f"{triangles['yellowx']}{triangles['yellowy']}"


  ax[0,0].plot(red_triangle, 'r--o')
  ax[0,1].plot(blue_triangle, 'b:s')
  ax[1,0].plot(green_triangle, 'g-.*')
  ax[1,1].plot(yellow_triangle, 'y-p')

  plt.tight_layout()
  plt.show()

improved_separated()





#2 marks: the function data returns a list of dictionaries
#2 mark: the function improved_separated correctly reproduces the subplots