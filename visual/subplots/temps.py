#Using data from a csv file to output axes/subplots
#The file temps.csv will be used in this example, data is separated by comas

import matplotlib.pyplot as plt #imports plot module
import csv #imports csv module to handle csv files

def read_data():
  temps = {}

  with open("visual/subplots/temps.csv") as the_csvfile:
    csv_reader = csv.reader(the_csvfile, delimiter=',')
    for row in csv_reader:
      temps['week1'] = [csv_reader[0]]
      temps['week2'] = [csv_reader[1]]

  return temps

def run():
  data = read_data()

  fig, axs = plt.subplots(2, 1, sharex='all') #2 rows, 1 column 

  week1 = {data['week1']}
  week2 = {data['week2']}

  axs[0].plot(week1)
  axs[0].plot(week2)

  plt.tight_layout()
  plt.show()

