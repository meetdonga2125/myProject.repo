# What is tuple? Difference between list and tuple.



#list:-

# Lists are mutable
# The implication of iterations is Time-consuming	
# The list is better for performing operations, such as insertion and deletion.	
# Lists consume more memory	
# Lists have several built-in methods	


	

#Tuple:-

# Tuples are immutable
# The implication of iterations is comparatively Faster
# A Tuple data type is appropriate for accessing the elements
# Tuple consumes less memory as compared to the list
# Tuple does not have many built-in methods


# Creating a List with
# the use of Numbers
# code to test that tuples are mutable
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("Original list ", List)

List[3] = 77
print("Example to show mutability ", List)


# code to test that tuples are immutable

tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)

#-------------------------------------------------------------------------------------------------------------------------

# As tuples are stored in a single memory block therefore they don’t require extra space for new objects whereas the lists are allocated in two blocks, first the fixed one with all the Python object information and second a variable-sized block for the data.


import sys
a_list = []
a_tuple = ()
a_list = ["Geeks", "For", "Geeks"]
a_tuple = ("Geeks", "For", "Geeks")
print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))


# Tuple consumes less memory as compared to the list



