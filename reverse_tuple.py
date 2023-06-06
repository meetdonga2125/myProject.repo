# Write a Python program to reverse a tuple.


t = ("Mysql", 2, "Postgraze", "MongoDB", 5, 0.2, "Sql")


# First convert a tuple into list...........................
l = list(t)

# afterthat we reverse a list by reverse method...............................
l.reverse()

# Now we convert list into tuple........................................
t1 = tuple(l)

print("reverse tuple is --> ", t1)



#Method-2---------------------------------------------------

# Reversing a tuple using slicing technique
# New tuple is created
def Reverse(tuples):
	new_tup = tuples[::-1]
	return new_tup
	
# Function call
tuples = ('p','y','t','h','o','n')
print(Reverse(tuples))


#Method-3---------------------------------------------------------

# Using lambda Function

Reverse_tuple = lambda tuples: (tuples[::-1])
print(Reverse_tuple(('p','y','t','h','o','n')))

