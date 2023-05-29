# Write a Python program to split a list into different variables


# initializing list
test_list = [1, 4, 5, 6, 7, 3, 5, 9, 2, 4]

# initializing split index list
split_list = [2, 5, 7]

# printing original list
print("The original list is:", test_list)

# printing original split index list
print("The original split index list:", split_list)

# using the slice function to split the list
res = []
start = 0
for end in split_list:
	res.append(test_list[slice(start, end)])
	start = end
res.append(test_list[slice(start, len(test_list))])

# printing result
print("The splitted lists are:", res)
#This code is contributed by Edula Vinay Kumar Reddy

list = [1,2,3,4,56,6,78]
list1 = list[slice(0,3)]
print(list1)