#Multiple nested decisions
print()
print("Beep is looking for his spare battery and needs some direction.")
print("Where should I look?")
print()
print("Bedroom /","Bathroom /","Lab")
place = input()
print()
print()

if place == "bedroom":
  print("Where in the bedroom should I look?")
  print()
  print("Under the bed /", "Wardrobe /", "Chest of drawers")
  bed = input()

  if bed == "under the bed":
    print()
    print("Found some shoes but no battery.")
  else:
    print()
    print("Found some mess but no battery.")

#Nested elif statements can be used with the whole if statement too
elif place == "bathroom":
  print("Where in the bathroom should I look?")
  print()
  print("Bathtub /", "Shower /", "Sink")
  bathroom = input()
  
  if bathroom =="bathtub":
    print()
    print("Found a rubber duck but no battery.")
  else:
    print()
    print("Found a wet surface but no battery.")


elif place =="lab":
  print("Where in the lab should I look, on the table perhaps?")
  print()
  print("Table /", "Lockers /", "Toolbox")
  lab = input()

  if lab == "table":
    print()
    print("Yes! I found my battery!")
  else:
    print()
    print("Found some tools but no battery.")


else:
  print("I do not know where that is but I'll keep looking.")

