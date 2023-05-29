# Write a Python program to unzip a list of tuples into individual lists


# Python3 code to demonstrate
# Unzip a list of tuples
# using zip() and * operator

# Initializing list of tuples
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]

# Printing original list
print("Original list is : " + str(test_list))

# Performing unzipping
# using zip() and * operator
res = list(zip(*test_list))

# Printing modified list
print("Modified list is : " + str(res))
