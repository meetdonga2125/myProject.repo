# Write a Python program to count the number of lines in a text file


file = open("count_file.txt",'w')
file.write('''
Hii Hello world
Good Morning
Good after noon
Good evening
Good Night
How have you been
Hello Python
Hello Java
Hello Django
Hello Javascript           
           ''')

file.close()


file = open("count_file.txt",'r')
file_count = file.readlines()
count = 0

for i in file_count:
    count += 1

print(count)    


#------------------------------------------------------------------

lines = len(file_count)
print(lines)