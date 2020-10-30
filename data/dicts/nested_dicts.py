def short_pattern():
  pattern = {
    "sequence":"101",
    "occurances":5}
  return pattern

def medium_pattern():
  pattern = {
    "sequence":"111000",
    "occurances":25}
  return pattern

def long_pattern():
  pattern = {
    "sequence":"1100110011001100",
    "occurances":50}
  return pattern
  
def run():
  print("Analysing patterns...")
  sequences = {
    "short sequence":short_pattern(),   #(1)
    "medium sequence":medium_pattern(),
    "long sequence":long_pattern()
    }

  for key, value in sequences.items(): #(2)
    print(f"{key}:{value}")

run()

#(1) The nested dictionaries, a dictionary inside a dictionary. In this case new "short, medium, long" sequences were created and they are paired with the calling of the precious functions which contain their own dictionaries to create a pair of key/value for the nested dictionary. 

#(2) It is nessessary to add the ".items()" function to the end of the dictionary variable, in this case "sequences", the .items() function unpacks all the items within the dictionary, especially if it is a large one like the nested dictionary above. Without using the function the progam will feedback an error message stating there is too many items to unpack.