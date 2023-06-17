#  Write a Python program to copy the contents of a file to another file

first_file = open("first_file.txt",'w')
first_file.write("Hello I am a content of first file")
first_file.close()


first_file = open("first_line.txt",'r')
second_file = open("second_line.txt",'w')
copy_content = first_file.read()

for line in copy_content:
    second_file.write(line)
    
first_file.close()
second_file.close()

show_first_file = open("first_file.txt",'r')
print(show_first_file.read())
show_first_file.close()

show_second_file = open("second_line.txt",'r')
print(show_second_file.read())
show_second_file.close()    
    