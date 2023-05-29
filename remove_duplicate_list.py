# Write a Python program to remove duplicates from a list.


list1 = [10,20,20,30,54,21,65,89,20,54]

# Python code to remove duplicate elements
def new_list(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
	
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(new_list(duplicate))
