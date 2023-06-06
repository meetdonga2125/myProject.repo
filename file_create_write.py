#  What is File function in python? What is keywords to create and write
# file.


#creating a text file with the command function "x"

f = open("createfile.txt", "x")
f.close()

f = open("createfile.txt", "w")
f.write('''Hello world!!!!!!!!!
        Good morning
        How are you
        what is your name
        where are you living''')
f.close()

