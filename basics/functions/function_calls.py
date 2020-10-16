#Beep and Bop have found a treasuremap in the book and it contains some cryptic words and markings. A program is neded to decipher the words and markings.

#The use of multiple function calls


def display_box(word):
  dashes_needed = 6 + len(word) #added vale for the "dashes_needed",3 spaces either side of the word so 6 space intotal and then plus the length of the word len(word).

  print("-" * dashes_needed)
  print("|  {}  |".format(word))
  print("-" * dashes_needed)



def display_lowercase(word):
  print (word.lower())
#(word.lower()) will make the parameter lowercase no matter how the user types in the input

def display_uppercase(word):
  print (word.upper())
#(word.upper()) will make the parameter uppercase no matter how the user types in the input

def display_mirrored_word (word):
  reverse_word =""
  for letter in reversed(word):
    reverse_word += letter

  print ("{} | {}".format(word, reverse_word))
 #Simply using the reversed() function will only give an object, a load of numbers and random letters, in the console and not the actual outcome wanted.

 #To use the "reversed" function, a variable with a value must be defined first. In this case the value is "reversed_word" which will have the value of an empty string. 

 #There are multiple ways of getting the outcome of trying to get a reverse word but in this case a for loop is used. The loop will take the each letter within the word and will reverse them "for letter in reversed(word)."

 #"reverse_word += letter" will take the word and give the letters in reverse, as definded in the for loop.



def repeat (word):
  print("How many times would you like the word to be displayed?")
  times_displayed = int(input())

  for versions in range (times_displayed): #Program will count up one at a time for the input variable
    if (versions % 2 == 0): # "% 2 == 0" the % 2 is divded by 2 and == 0 is equal to zero
      display_lowercase(word)
    else:
      display_uppercase(word)


def run():
  print("Enter a word to be displayed.")
  word = input()
  display_box(word)

  print ("The word mirroed:")
  display_mirrored_word(word)
  print()

  repeat(word)




#run()



#Calling of the defined functioned

#display_box("hello how are you?")
#display_lowercase("HELLO")
#display_uppercase("hello")
#display_mirrored_word("Goodbye")
#repeat("hello")

