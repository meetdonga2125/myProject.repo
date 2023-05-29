# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings.

char_string =  input("Enter a string: ")

new_char_string = char_string.split(" ")
# print(new_char_string)

string = 0

for i in new_char_string:
    
    
    if len(i)>2 and i[0]==i[-1]:
        string += 1
        
print(string)            