#Program to calculate the users body-mass index (bmi).

def run():
  
  print()
  print("What is your name human?")
  print("Please enter name.")
  name = input()
  print()
  print("How old are you (in years)?")
  print("Please enter age.")
  age = int(input())
  print()
  print("How tall are you (In meters)?")
  print("Please enter height.")
  height = float(input())
  print()
  print("How much do you weigh (in kilograms)?")
  print("Please enter weight.")
  weight = float(input())

  bmi = weight / height ** 2
  print()
  print("{} you are".format(name),"{} years old".format(age),"and your BMI is {:.2f}.".format(bmi))