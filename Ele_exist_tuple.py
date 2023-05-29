# Write a Python program to check whether an element exists within a
# tuple


Tuple = (10,20, "python", 0.2, False, 0, "Java")

for i in Tuple:
    if (i=="python"):
        print("Yes, I am ")
    else:
        print(i)    
        
#----------------------------------------------------------------------- 

       
print("python" in Tuple)
print("java" in Tuple)        
print(0 in Tuple)



#===========================================================================
#Method-3

# Python3 code to demonstrate working of
# Check if element is present in tuple
# using loop

# initialize tuple
initi_tuple = (10, 4, 5, 8)

# printing original tuple
print("The original tuple : " + str(initi_tuple))

# initialize n
n = 6

# Check if element is present in tuple
# using loop
res = False
for ele in initi_tuple:
	if n == ele:
		res = True
		break
else:
    print(ele)

# printing result
print("Does tuple contain required value ? : " + str(res))
