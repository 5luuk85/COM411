#Bop is still trying to climd the ladder while Beep is busy reading the book.
#A program needs to be created in order to help Bop distribute the weight while climbing.

def sum_weights(beep_weight, bop_weight):
  total_weight = beep_weight + bop_weight
  return total_weight
#REMEMBER the return value HAS to be the variable set i.e. "total_weight", otherwise it will NOT work later on, so in this case we need to "return total_weight".
def calc_avg_weight (beep_weight, bop_weight):
  average_weight = (beep_weight + bop_weight) / 2
  return average_weight

def run():
  print("Plese enter the weight for each robot.")
  print("Beep's weight:")
  print()
  beep_weight = float(input())

  print()
  print("Bop's weight:")
  print()
  bop_weight = float(input())

  print("What would you like to calculate (sum or average)?")
  response = input()
  print()

  if response =="sum":
    answer = (sum_weights(beep_weight, bop_weight))
    print ("The sum weight of Beep and Bop is: {:.2f}".format(answer))

  elif response =="average":
    answer = (calc_avg_weight(beep_weight, bop_weight))
    print ("The average weight of Beep and Bop is: {:.2f}".format(answer))
  else:
    print("Invalid, please try again.")

#run()