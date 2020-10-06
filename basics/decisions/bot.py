#The use of an elif statement with if and else statements

print("Towards which direction should I paint (up, down, left or right)?")
direction = input()


if direction ==("up"):
  print("I am painting the upward direction!")

#Any amount of elif statements can be used
elif direction ==("left"):
  print("I am painting towards the left!")
elif direction ==("right"):
  print("I am painting towards the right!")
elif direction ==("down"):
  print("I am painting downwards!")

#Only one else statement can be used, normally to close up
else:
  print("I don't know which direction you want me to go!") 