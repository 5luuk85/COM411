#The use of a membership operator within a for loop. In this case "in". 

print("""What phrase do you see?
""")
phrase = input()
print()

#reverse variable is a string
reverse = ""

print("Reversing... The phrase is...", end="")

#The "in" operator will evaluate if the values in "phrase" is true. In this case, because "in" has no set limitation, it will evaluate the variable "phrase" as true.
for letter in phrase:
  reverse = letter + reverse
#for the local variable "letter" 
print(reverse)
  