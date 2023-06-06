#  Write a Python program to read a random line from a file.





import random

with open("file.txt","r") as file:
    lines = file.read().splitlines()
    print(random.choice(lines))
    
    
#------------------------------------------------------    

import random
lines = open('file.txt').read().splitlines()
myline =random.choice(lines)
print(myline)

#------------------------------------------------------

# read_file = open('file.txt','r')
# print(read_file.read())
# read_file.close()

#-----------------------------------------------------

# write_file = open('file.txt', 'w')
# write_file.write("what about you?")
# write_file.close()


