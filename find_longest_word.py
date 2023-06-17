#  Write a python program to find the longest words

file = open("longest_word.txt",'w')
file.write("Python is a very easy and versatile language")
file.close()


file = open("longest_word.txt",'r')
l = file.read().split()
print(l)
max_len = len(max(l, key=len))
print(max_len)

for word in l:
    
    if len(word)==max_len:
        print(word, "is a longest word in all words")
    


file.close()