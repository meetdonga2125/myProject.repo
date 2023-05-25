# How will you compare two lists?

# Compare two list by sort method................

l1 = ["Mango", "Banana", "Grapes", "Watermelon", "Kiwi", "Pinaple"]
l2 = ["Berlin", "Jakarta", "Delhi", "Colombo", "Helsinki", "Stockholm", "Copenhagen"]
l3 = ["Jakarta", "Delhi", "Colombo", "Copenhagen", "Helsinki", "Berlin", "Stockholm"]


l1.sort() 
l2.sort() 
l3.sort() 

# print(l1)
# print(l2)
# print(l3)

if l1 == l2: 
    print ("The lists l1 and l2 are the same") 
else: 
    print ("The lists l1 and l2 are not the same") 
    

if l2 == l3: 
    print ("The lists l2 and l3 are the same") 
else: 
    print ("The lists l2 and l3 are not the same")    

if l1 == l3: 
    print ("The lists l1 and l3 are the same") 
else: 
    print ("The lists l1 and l3 are not the same")
    
  