file = open("ExampleTextFile.txt",'w')
file.write('''
Good Morning Tops Technologies
This is  Tops technologies sample File
Consisting of Specific
abbreviated
source codes in Python
Imagination
Summary and Explanation
Welcome user
Learn with a joy
           ''')
file.close()

# input text file
inputFile = "ExampleTextFile.txt"

# Enter N value
N = int(input("Enter N value: "))

# Opening the given file in read-only mode
with open(inputFile, 'r') as filedata:

# Read the file lines using readlines() 

  linesList = filedata.readlines()
  print("The following are the first",N,"lines of a text file:")

# Traverse in the list of lines to retrieve the first N lines of a file
for textline in (linesList[:N]):

# Printing the first N lines of the file line by line.
   print(textline, end ='')

# Closing the input file
filedata.close()