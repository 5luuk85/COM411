#Subplots are also known as axes, not to be confused with axis. Both different things.

#The things that make plotting subplots possible is the figure and followed by the axes.
#The figure is the container or overall display, and then the axes is the actual plots/graphs themselves. Later on the figure is refered to as "fig" and the axes; "axs" in the coding.

import matplotlib.pyplot as plt #import plot module

def read_data(file_path):

  with open (file_path) as file:
    temps_list = [] #empty list

    for lines in file.readlines(): #Reads the individual lines in the file
      temps_list.append(int(lines.strip())) #.strip removes all the empty spaces in the text file when 

  return temps_list

def run():
  data = read_data("visual/subplots/temps.txt") #path of file

  fig, axs = plt.subplots(1, 2, sharex='all') #"sharex='all'" = all subplots share the x-axis, 1, 2 = 1 row 2 columns

  x = range (0, 7, 1) #Set values for x-axis 
  y = data #Using data from called function

  plt.xlabel("Day") #Labeling the axis
  plt.ylabel("Temperature") 

 
  axs[0].plot(x, y) #"[0]" indicates the first graph on the same horizontle display/figure
  axs[1].bar(x, y) #"[1]" indicates the second graph on the same horizontle display/figure

  plt.tight_layout() #When displaying multiple plots, displays such as the labels can often be overlapped by another plot due to the sizing of the display, the ".tight_layout()" function makes sure the plots are properly size not to overlap. 

  plt.show() #Always include brackets with the ".show" function or it will NOT work

run()