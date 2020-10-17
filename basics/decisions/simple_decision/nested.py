#Nested  decisions. Where an if statement has an additional if statement indented below the first statement. This is to allow multiple choices within an if statement.

def run():

  print("What type of book cover does the book have?")
  print("soft/hard")
  cover = input()
  print()
  if (cover =="soft"):
    print("Is the cover perfect bound? (Yes/No)")
    answer = input() 
    if (answer == "yes"):
      print("Soft cover, perfect bound books are very popular!")
    else:
      print("Soft covers with coils or stitches are great for short books.")
  else:
    print("Books with hard covers can be more expensive!")


    