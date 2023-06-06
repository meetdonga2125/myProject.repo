# Write a Python script to check if a given key already exists in a
# dictionary


info = {"Name":"Meet", "City":"Gandhinagar", "hobby":"cricket", "state":"Gujarat"}

info1 = {"Name": "Kartik"}

# info["Name"] = "Kartik"

print(info1.keys())

if "Name" in info.keys():
    print("I am already exist in info")
else:
    print("I am not exist")    
    
    
info_list = list(info.keys())

info1_key = "Name"
res = "Not present"
if info_list.count(info1_key)==1:
    res = "Present"
print("I am already exist")    



#-------------------------------------------
#second method

# Python3 Program to check whether a
# given key already exists in a dictionary.

def checkKey(dic, key):
	if key in dic.keys():
		print("Present, ", end =" ")
		print("value =", dic[key])
	else:
		print("Not present")
		

dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)

key = 'w'
checkKey(dic, key)
