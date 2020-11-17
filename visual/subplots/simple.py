import matplotlib.pyplot as plt

def read_data(file_path):

  with open (file_path) as file:
    temps_list = []

    for lines in file.readlines(): #Reads the individual lines in the file
      temps_list.append(int(lines.strip()))

  return temps_list

def run():
  data = read_data("visual/subplots/temps.txt")

  fig, axs = plt.subplots(1, 2, sharex='all') #all subplots share the x-axis, 1, 2 = 1 row 2 columns

  x = range (0, 7, 1)
  y = data

  plt.xlabel("Day") #Labeling the axis
  plt.ylabel("Temperature") 

 
  axs[0].plot(x, y)
  axs[1].bar(x, y)

  plt.tight_layout()
  plt.show()

run()