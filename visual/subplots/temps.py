#Using data from a csv file to output axes/subplots
#The file temps.csv will be used in this example, data is separated by comas
#CSV = Comma Separated Values
import matplotlib.pyplot as plt #imports plot module
import csv #imports csv module to handle csv files

key_week1 = None #Global variables, can be used throughout the code
key_week2 = None #Should be avoided to cause less confusion for user and python itself but in some cases it makes sense to use them


def read_data():
  global key_week1, key_week2 
  #defines the usesage of global variables, since there are variables with the same name in local blocks of code in this example

  with open("visual/subplots/temps.csv") as the_csvfile:
    csv_reader = csv.reader(the_csvfile, delimiter=',') #By deault the csv reader delimits commas, so it isn't nessessary to put it in the code but this example shows it.

    header = next(csv_reader) #the "next" function will read the first line and start from the next line. It's useful when a file contains headings.

    #Useful to assign the headers to separate variables and use the ".strip" function early on to remove empty white gaps in the file. Implementing the ".strip" early on to the specific data, the headers in this case, will ensure the strip function is not needed to be repeated later on.
    key_week1 = header[0].strip() 
    key_week2 = header[1].strip() 

    

    temps = {       #Dictionary created
      key_week1:[], #The key "header[0]" is "week1" in the csv file
      key_week2:[]  #The key "header[1]" is "week2" in the csv file
    }               
                    #Remember a dictioary is -> [Key]:[Value]

    for row in csv_reader:
      temps[key_week1].append(row[0].strip())
      temps[key_week2].append(row[1].strip()) 
      #always remember to use ".strip" when using files with empty spaces

  return temps

def run():
  data = read_data() #Calling the first function to be stored in a variable

  fig, axs = plt.subplots(2, 1, sharex='all') #2 rows, 1 column 

  week1 = (data[key_week1]) #Assigning dictionary to variables
  week2 = (data[key_week2])

  plt.xlabel("Days")        
  plt.ylabel("Temperature") #Giving the axis a label

  axs[0].plot(week1) #First plot
  axs[1].plot(week2) #Second plot

  plt.tight_layout()
  plt.show()

run()
