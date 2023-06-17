#  Write a Python program to read a file line by line and store it into a list


file = open("store_list.txt",'w')
file.write('''
Hello what is your name
where are u living
what is birth_date
which is your favourite Game?
what is your hobby
which is your favourite book
which is your favourite place      
           ''')
file.close()

file = open("store_list.txt",'r')
file_list = file.readlines()

store_list = []
for item in file_list:
    store_list.append(item)

print(store_list)    
    