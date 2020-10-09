#Example of the while loop with the end="" function with ascii art.

print("""
How many bars should be charged?
""")

bars = int(input())
charge = 0

print()
while (charge < bars):
  charge +=1
  print("Charging:", end="")
  print("▌" * charge)
  print()


print ("The battery is fully charged.")