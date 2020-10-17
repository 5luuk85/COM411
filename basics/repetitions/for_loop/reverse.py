#Indexing a string in reverse

def run():

  print("What phrase do you see?")
  phrase = input()

  print("Reversing the phrase...")


  print("The phrase is...", end="")

  for reverse in range (len(phrase) -1, -1 ,-1):
    print(phrase[reverse], end="")