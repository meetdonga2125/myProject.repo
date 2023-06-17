#  Write a Python program to write a list to a file.

language_list = ["Python","Java","Node","React","Express","Php","laravel","Django","React","HTML", "CSS"]

file_list = open("write_list.txt", 'w')

for language in language_list:
    file_list.write(language + "\n")
    
file_list.close()

file_list = open("write_list.txt",'r')
print(file_list.read())
file_list.close()