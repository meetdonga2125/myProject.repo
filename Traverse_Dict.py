# How Do You Traverse Through A Dictionary Object In Python?


myDict = {}
myDict["ID"] = "101"
myDict["Name"] = "Tom"
myDict["City"] = "Gandhinagar" 
print(myDict) 


for i in myDict:
    print(i)
    
for i in myDict.items():
    print(i)
    
for i in myDict.keys():
    print(i)
    
for i in myDict.values():
    print(i)