#The use of a for loop. 

def run():

  print("How many mountains should I display?")
  mountains = int(input())

  print("Displaying mountains...")

  #The "mountain" variable is only local to this for loop and it cannot be used outside of the loop. The "mountains" variable is from the user input. The "range function is a function that will determine a number up to the the value of the user inputed variable "mountains". 
  for mountain in range(mountains):
  
  print("""           
        __
      /  \\_  
      /^    \\
    /  ^    \\_
  _/ ^ ^     ^\\
  /  ^     ^   \\
    """)
