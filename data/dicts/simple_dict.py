#Dictionaries are defined by curly brackets {}. 

#Dictionaries store data in groups of keys and values. The key and value are separated by a colon ":". Curly brackets without a group of keys and values, such as just strings are just sets, refer back to the simple_set.py file in the sets folder for an example.

#(a) When coders are defining a dictionary with data, they often list them, shown below, to make it easier to look at when there is a lot of data within the dictionary.

def pattern():
  sequences = {
    "Short Sequence":3, #(a)
    "Medium Sequence":2, 
    "Long Sequence":1} 

  return sequences

def run():
 print( pattern() )

run()