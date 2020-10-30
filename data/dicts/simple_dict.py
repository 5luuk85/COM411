#Dictionaries are defined by curly brackets {}. 

#Dictionaries store data in groups of keys and values. The key and value are separated by a colon ":". Curly brackets without a group of keys and values, such as just strings are just sets, refer back to the simple_set.py file in the sets folder for an example.


def pattern():
  sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}

  return sequences

def run():
 print( pattern() )

run()