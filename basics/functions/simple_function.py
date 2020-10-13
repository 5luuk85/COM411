#Program that listens for sounds in the cave where beep and bop are in.
#Defining a function using "def" and call it in order to display the output of the function.


#The defined function I have created is "listen", below is what the function does.
def listen ():
  print("""What sound did I hear?
  """)
  sound = input()

  if sound =="rumble":
    print("That was a loud rumble!")
  else:
    print("It was probably nothing.")

#Simply running the custom defined function will not do anything over in the console, it will only run in the background. But if we call it, as shown below, the function will then run on the console.
listen()