# Write a Python program to check whether a list contains a sub list

# Python3 code to demonstrate working of
# Check for Sublist in List
# Using loop + list slicing

# initializing list
test_list = [5, 6, 3, 8, 2, 1, 7, 1]

# printing original list
print("The original list : " + str(test_list))

# initializing sublist
sublist = [8, 2, 1]

# Check for Sublist in List
# Using loop + list slicing
res = False
for idx in range(len(test_list) - len(sublist) + 1):
	if test_list[idx: idx + len(sublist)] == sublist:
		res = True
		break

# printing result
print("Is sublist present in list ? : " + str(res))


#Method-2---------------------------------------------------------

# Python3 code to demonstrate working of
# Check for Sublist in List

# initializing list
test_list = [5, 6, 3, 8, 2, 1, 7, 1]

# printing original list
print("The original list : " + str(test_list))

# initializing sublist
sublist = [8, 2, 7]

# Check for Sublist in List
c=0
res=False
for i in sublist:
	if i in test_list:
		c+=1
if(c==len(sublist)):
	res=True
# printing result
print("Is sublist present in list ? : " + str(res))

