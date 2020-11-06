
#".strip()" removes any coding if something is being written into a file. Writting a line into a new file will produce the string "\n" so adding ".strip()" will remove that unwanted coding in the file.

def search(the_file):
  print("Searching...", end="")
  data = {}

  with open(the_file) as file:
    section ="" #empty variable created for the loop 

    for line in file:
      if line.startswith("Section"):
        section = (line.split(":")[1]).strip() #[1] 
        
      else:
        if section in data:
          data[section].append(line.strip()) #[2]
        else:
          data[section] = [line.strip()] #[3]

#[1] Defines the second part of the "section:*book*" in the book.txt we are after
#[2] The If statement will go through the list of books, if a new book is found, it is added to the list
#[3] If a new book is found with a new section, then the section and book is added to the dictionary

  print("Done!")
  return data

def run():
  data = search("data/files/txt/books.txt")
  with open("data/files/txt/generated.csv", "w")as file:
    for section, books in data.items(): #[4]
      for book in books:#[5]
        file.write(f"{section}, {books}\n") #"\n" will write the lines on a new line in the file

#Nested for loop
#[4] First for loop will get the secions of the dictionary "data", ".items" will instruct the code to look through each individual item as an entity in the dictionary
#[5] Second for loop will get the the individual books within the dictionary

run()