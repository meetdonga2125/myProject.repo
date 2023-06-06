#  Write a Python program to create a tuple with numbers


intTuple = ()
number = int(input("Please enter the Total Tuple Items to store :  "))
for i in range(1, number + 1):
    value = int(input("Please enter Tuple Item :  "))
    intTuple += (value,)

print("Tuple Items : ", intTuple)

    
#---------------------------------------------------------------------------
   
Tuple = (10,20,30,45,21,526,21,45,21,0,52)    
New_tuple = ()
for i in Tuple:
    New_tuple += (i*i,)
    
print(New_tuple)    

#----------------------------------------------------------------------------

New_tuple = tuple(i*i for i in range(10))
print(New_tuple)