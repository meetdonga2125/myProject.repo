# Write a Python program to convert a list of tuples into a dictionary.


tuples = [(1,2),(2,3),(3,4),(4,5)]
dic = dict(tuples)
print(dic)


# Python code to convert into dictionary

print(dict([('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]))



# Method-2--------------------------------------------------------------

# Python code to convert into dictionary

def Convert(tup):
	di = dict(tup)
	return di
	
# Function call

tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
	("suraj", 20), ("akhil", 25), ("ashish", 30)]
# dictionary = {}
print(Convert(tups))


