#Program to tell Beep to avoid the amount of live wires.

#The use of an end parameter, the print function will go onto the next line down after it has been read. The end="" function overides this and will read the next string on the next line down into the empty string("") after the function is stated. 

print("""
How many live cables must I avoid?
""")
live_cables = int(input())
avoid = 0

print()
while (avoid < live_cables):
<<<<<<< HEAD
  avoid = avoid +1
  print ("Avoiding...", end="")
  print ("Done! {} live cables avoided.".format (avoid))
  
=======
  print ("Avoiding...", end="")
  print ("Done! {} live cables avoided.".format (avoid))
  avoid = avoid +1
>>>>>>> 43f549e461abcd5d2201474c1b5952116fa4157a


print("""
All live cables have been avoided.""")