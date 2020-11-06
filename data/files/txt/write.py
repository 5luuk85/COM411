#Writing to a file, creating a lists of different content in a new file.
#The file books.txt has been created and has preloaded content in it. The sections are defined by a tuple "Section: *name of section*" and then followed by the books in the lines under.
#This program will sort the data within that file. The different sections will be listed in one list and the books in another.


def search(the_file):
  print("Searching...", end="")
  sections = []
  books = []

  with open (the_file) as file:
  
    for line in file:
      if line.startswith("Section"): #".startswith" defines the starting of a line
        name_of_section = line.split(":")[1] #[1]
        sections.append(name_of_section.strip()) #[2]
    
      else:
        books.append(line.strip()) #[2]
  
  print("Done!")
  return sections, books #The data gathered in the lists are returned to the function as a tuple as they are two lists and the lists are separted by a comma. "sections" is in the first position of the tuple while "books" is in the second part of the tuple. 

#[1] The file which is defined later on in the code is book.txt. The file contains tuples such as "Section:The Law Section". From the condition set by the if statement above, If the line contains the string "Section" which is part of the tuple within the file then the ".split" function will split that data, the colin ":" specifies where to split the data. Finally the "[1]" is the position of the data we wish to extract, in this case it's the second part of the tuple.
#[2] When writing out the contents to a new file, any coding that is carried will also be written in the file itself. In this case,the code is checking for lines and the "\n" coding will also be written into the file. To stop this the ".strip()" function can be added.


def save(the_file, data):
  print("Saving...", end="")

  with open(the_file, "w") as file: #[3]
      file.write(f"Sections: {data[0]}\n") #[4]
      file.write(f"Books: {data[1]}\n")  #[4]

  print("Done!")

#[3]The added "w" in the "with open" file function specifies the file is open and to be written in
#[4] ".write" is the write to file function, the file will need to be specified before the ".write" function. In this case we are writting formatted strings into the file. In the last part of the code, the parameter is defined as the tuples from the first function, therefore the positions of the tuples in the data are specified with [0] and [1] in the {data} tuples. The "\n" is added because the ".write" function will write the formatted strings all on the same line in the new file by defualt. 

def run():

  #Calling the functions 
  data = search("data/files/txt/books.txt") #[5]
  save("data/files/txt/section-books.txt", data) 
  
  #[5] The variable "data" is defined by the "search" function

  #If the file does not exist already, a new file will be created with the specified directory and file name in the code, in this case "section-books.txt" is created under the specified file path.

run()