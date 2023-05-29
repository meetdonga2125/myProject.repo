#  Write a Python program to find the repeated items of a tuple

a = (1,2,3,45,6,1,2,4,8,9,45,0,4)
b = []
repeated_tuple = ()
for i in a:
    if i not in b:
        b.append(i)
    else:
        repeated_tuple += i,
        
print("repeated tuple element is: ", repeated_tuple)    


       