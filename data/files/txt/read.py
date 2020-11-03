def search(the_file):
  print("Searching...")

#Note the file name in this case will have to be the parameter as later on in the run function, we are specifying the path and the exact file.

  with open(the_file) as file:
    for line in file:
      print (f"Looked in {line}", end="")
  
  print("\n...Done!")

def run():
  search("data/files/txt/locations.txt")
  
run()