#  Write a Python program to remove an empty tuple(s) from a list of tuples


list_of_tuple = [(1,2),(2,3),(3,4),(), (4,5), (5,6),()]

for i in list_of_tuple:
    if i==():
      list_of_tuple.remove(i)
    
print(list_of_tuple)        



#With Function---------------------------------------------------

# Python program to remove empty tuples from a
# list of tuples function to remove empty tuples
# using len()


def Remove(tuples):
	for i in tuples:
		if(len(i) == 0):
			tuples.remove(i)
	return tuples


# Function call
tuples = [("fronted", "HTMl"), ("fronted", "CSS"), (), ("Backend", "Python"), ("Framework", "Django"),(),]
print(Remove(tuples))


#lambda 

empty_tuple = list[lambda tuples: (tuples.remove(i) for i in tuples if len(i)==0 )]

print((empty_tuple([("fronted", "HTMl"), ("fronted", "CSS"), (), ("Backend", "Python"), ("Framework", "Django"),(),])))
