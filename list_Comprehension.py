#eg.1----------------------------------------------------------------------------------------------------------
list = [character for character in [1,2,3]]

print(list)



#eg.2---------------------------------------------------------------------------------------------------------
l=[]
for i in range(1,100):
    l.append(i)
print(l)

# list comprehension

List = [i for i in range(1,100)]    
print(List)



#eg.3-------------------------------------------------------------------------------------------------------------

List = [i for i in range(1,100) if i%2==0]
print(List)


#eg.4-----------------------------------------------------------------------------------------------------------

matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

print(matrix.index([0,1,2]))


#eg.5------------------------------------------------------------------------------------------------------------

lst = [i*i for i in range(1,20) if i%2==0]
print(lst)

lst.append(400)
print(lst)

#eg.6---------------------------------------------------------------------------------------------------------------

list_1 = [1,32,4,5,45,4,4,3,3,3,5,6,65,6,643,65,5,4,21,58,95]
divide_by_3 = []
for item in list_1:
    if item%3 == 0:
        divide_by_3.append(item)
print('Without using list comprehensions', divide_by_3)   

#By using list comprehension

print("Using List comprehension", [item for item in list_1 if item%3==0])


#eg.7----------------------------------------------------------------------------------------------------------------------

myFood = ["Apple", 2,3, "Orange", 89, "Mango", "56",65]

nonInt = []

# Without using List comprehension

for item in myFood:
    if not str(item).isdigit():
        nonInt.append(item)
print(nonInt) 

# With list comprehension

nonInt = [item for item in myFood if not str(item).isdigit()]
print(nonInt)

#eg.8-----------------------------------------------------------------------------------------------------

print([str(item).lower() for item in myFood])
print([str(item).upper() for item in myFood])
print([str(item).capitalize() for item in myFood])
print([str(item).count("2") for item in myFood])


#eg.9.................................

A = [1,3,5,7]
B = [2,4,6,8]

cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)

# eg.10

fruits = ["apples", "bananas", 5]
print([i.upper() for i in fruits if type(i) == str])

#eg.11
my_string = "HelloMyNameIsMeet"
my_string = "".join([i for i in my_string])
print(my_string)

my_string = "".join([i if i.islower() else " " + i for i in my_string])[1:]
print(my_string)


#eg.12

# Without List Comprehension 
fruits = ["apple", "cherry", "Grapes", "Mango", "Orange", "Kiwi"]

list1 = []
for fruit in fruits:
     if "a" in fruit:
         list1.append(fruit)

print(list1)  

      
         
         
# With List Comprehension        
list1 = [fruit for fruit in fruits if "a" in fruit]  
print(list1)    



#eg.13

list2 = [str(x).isdigit() for x in range(10)]   
print(list2)

#eg.14

a = int(input("Enter a value: "))
list3 = [i*a for i in range(1,11)]
print(list3)


#eg.15

import random

l = [random.randint(1,100) for i in range(11) ]
print(l)



         


      




