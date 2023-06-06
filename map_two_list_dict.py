# Write a Python program to map two lists into a dictionary


# Python3 code to demonstrate
# conversion of lists to dictionary
# using dictionary comprehension

# initializing lists
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

# using dictionary comprehension
# to convert lists to dictionary
res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))

#----------------------------------------------------------------------------------------


# Python3 code to demonstrate
# conversion of lists to dictionary
# using zip()

# initializing lists
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

# using zip()
# to convert lists to dictionary
res = dict(zip(test_keys, test_values))

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))


#---------------------------------------------------------------------------------------------

# Python3 code to demonstrate
# conversion of lists to dictionary
# using naive method

# initializing lists
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

# using naive method
# to convert lists to dictionary
res = {}
for key in test_keys:
	for value in test_values:
		res[key] = value
		test_values.remove(value)
		break

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))

