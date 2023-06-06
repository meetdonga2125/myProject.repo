# Write a Python program to combine two dictionary adding values for
# common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).


dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'c': 400}

# Python program to combine two dictionary
# adding values for common keys
# initializing two dictionaries



# adding the values with common key
for key in dict2:
	if key in dict1:
		dict2[key] = dict2[key] + dict1[key]
	else:
		pass
		
print(dict2)
