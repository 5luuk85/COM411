import random

print("Please enter the minimum value.")
minimum_value = int(input())

print("Please enter the maximum value.")
maximum_value = int(input())

random_no = random.randrange(minimum_value, maximum_value)

print("I am thinking of a number between {} and {}. Can you guess what the number is?". format(minimum_value, maximum_value))

guess = 0

while (guess != random_no):
  print("Please enter number.")
  guess = int(input())
  
  if (guess == random_no):
    print("Congratulations! You guessed my number!")
    break

  elif (guess < random_no):
    print("Your guess is too low!")

  elif (guess > random_no):
    print("Your guess is too high!")

print("Game over!")
  