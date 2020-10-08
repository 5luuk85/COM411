#Using the "or" operator. Boolean logic will evalute if a statement is true or false, in this case the or operator will evalute a statement from left to right, both sides being true.

#Beep is feeling adventurous and wants us to pick route for him.

print("""What type of adventure should I have?

Scary / Short / Safe / Long
""")
adventure = input()

print()
if ((adventure == "scary") or (adventure == "short")):
  print("Entering the dark forest!")

elif((adventure == "safe") or (adventure =="long")):
  print("Taking the safe route!")

#The or statement in this case is reading the variable adventure as true for both sides.

else:
  print("Not sure which route to take.")
