#Finding a character and it's position in a sequence of a string or text.

print("Please enter a sequence.")
sequence = input()

print("Please enter a character for the marker.")
marker = input()

#Variables for the positions of the markers need to be added for loop to work out the values of the position.
marker1_pos = -1 #-1 means invalid position, the position has no value.
marker2_pos = -1

for character in range (0, len(sequence), 1):
  pos = sequence[character] #[character] is the local variable in for statement above.

  if (pos == marker):
    if (marker1_pos == -1):
      marker1_pos = character
    else:
      marker2_pos = character

  

print("The distance between the markers is", marker2_pos - marker1_pos - 1)