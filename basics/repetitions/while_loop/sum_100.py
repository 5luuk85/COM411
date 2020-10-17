#Using the while loop to calculate the sum of the first 100 numbers.
def run():

  print("Calculating the sum of the first 100 numbers...")

  number = 1

  total = 0

  while (number <= 100):
    total = total + number
    number = number + 1

  print("...Done! the total is", total)