def run(): 
 
  print("What level of brightness is required?")
  brightness = int(input())
  print()
  print("Adjusting brightness...")
  print()

  #The "level" variable is local to this for statement only. 
  #Within the range (1, brightness + 1), it is stating that the start of the sequence at 1, the range is between any number between 1 and the user inputs (brightness) value and the sequence will go up in increments of 1s with the "+ 1".
  for level in range (1, brightness + 1):
    print("Beep's brightness level:", "*" * level)
    print("Bop's bright level:", "*" * level)
    print()

  print("Adjustments complete!")