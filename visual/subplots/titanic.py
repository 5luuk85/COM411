#Using real life data for plots and subplots

import csv
import matplotlib.pyplot as plt

PassengerID = None  #Global variables set, should be avoided though if not nessessary
Survived = None
Pclass = None
Name = None
Sex = None
Age = None
SibSp = None
Parch = None
Ticket = None
Fare = None
Cabin = None
Embarked = None


def read_data():
  global PassengerID, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked #Making it clear to python that global variables are used

  with open("visual/subplots/titanic.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    PassengerID = header[0].strip()
    Survived = header[1].strip()
    Pclass = header[2].strip()
    Name = header[3].strip()
    Sex = header[4].strip()
    Age = header[5].strip()
    SibSp = header[6].strip()
    Parch = header[7].strip()
    Ticket = header[8].strip()
    Fare = header[9].strip()
    Cabin = header[10].strip()
    Embarked = header[11].strip()



    data = {      #Creation of Dictionary, remember the format for a dic -> [Key]:[Value]
      PassengerID:[],
      Survived:[],
      Pclass:[],
      Name:[],
      Sex:[],
      Age:[], 
      SibSp:[],
      Parch:[],
      Ticket:[],
      Fare:[],
      Cabin:[],
      Embarked:[]
    }

    for row in csv_reader:
      data[PassengerID].append(row[0].strip())
      data[Survived].append(row[1].strip())
      data[Pclass].append(row[2].strip())
      data[Name].append(row[3].strip())
      data[Sex].append(row[4].strip())
      data[Age].append(row[5].strip())
      data[SibSp].append(row[6].strip())
      data[Parch].append(row[7].strip())
      data[Ticket].append(row[8].strip())
      data[Fare].append(round(row[9], 2).strip())
      data[Cabin].append(row[10].strip())
      data[Embarked].append(row[11].strip())

  return data

def run():
  data = read_data()

  fig, axs = plt.subplots(2,2)

  PassengerID_dict = (data[PassengerID])
  Survived_dict = (data[Survived])
  Pclass_dict = (data[Pclass])
  Name_dict = (data[Name])
  Sex_dict = (data[Sex])
  Age_dict = (data[Age])
  SibSp_dict =(data[SibSp])
  Parch_dict = (data[Parch])
  Ticket_dict = (data[Ticket])
  Fare_dict = (data[Fare])
  Cabin_dict = (data[Cabin])
  Embarked_dict = (data[Embarked])

  axs[0].xlabel('Passenger')
  axs[0].ylabel('Fares')

  axs[0].title.set_text('Passenger Fares')

  axs[0].plot(PassengerID_dict, Fare_dict)

  plt.tight_layout()
  plt.show()

run()