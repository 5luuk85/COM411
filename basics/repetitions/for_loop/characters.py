def run():
  
  print("What strange markings do you see?")
  marking = input()
  print()
  print("Identifying...")

  print()
  for position in range(0, len(marking), 1): #The "len(marking)" indicates the length of the characters within the string of the user input "marking".
    print("Index", position, ":", marking[position])
  #The "marking[postition]" means the users string input "marking" and "position" is the inhouse variable in the for statement. The [] is a store of data.

  print("Done!")