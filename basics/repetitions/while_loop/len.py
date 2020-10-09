#Beep has fully charged the battery on the robot. Each time Beep speaks to the robit, it replies "bop". We wish to create a program that allows Beep and the robot to communicate.

#Use of the len() function.

print("""
Please enter a phrase.
""")
 
phrase = input()
length = len(phrase)
#len will read the number of characters within a string. In this case the variable "length" is the number of characters of the users input variable "phrase".

#Next we need a control variable for the while loop.
repeat = 0

print("""
The robot responds.
""")

while (repeat < length):
  print("bop ", end="")
  repeat +=1

