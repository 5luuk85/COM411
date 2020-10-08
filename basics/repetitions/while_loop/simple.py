#A "while statement is like an if statement but it will loop litself until the condition is false"

#Beep finds another robot while exploring the forest but it is entangled in cables. The robot is damaged. Beep should try to removed the cables from the trapped robot.

print("""
I need to free the robot from these cables.
How many cables should I remove?
""")

remove = int(input())
cables = 0
#The base number for the variable "cables" is 0, the user input variable "remove" will be a number. 

#The while loop will look at if the cables value is smaller than the remove value. A string statement will then be printed. The cables = cables + 1 will add a value of 1 to cable. Depending on the user input value for "remove" the "cables" value will be increase by 1 every time the loop is in effect. The print statement will also be run by the amount of times of the "remove" value.
while (cables < remove):
  print("Cables removed.")
  cables = cables + 1

