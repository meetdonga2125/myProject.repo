# Write a Python program to convert a list to a tuple

l = [10,20,30,"Python", "Java", "Django", "spring", 0.2, 0, True, 20, 0.2]

t = tuple(l)

print(t)


# Method-2-----------------------------------------------

# Python3 program to convert a
# list into a tuple

def convert(list):
	return tuple(list)

#Function call

list = [1, 2, 3, 4]
print(convert(list))

#Method-3 Using lambda Function----------------------------

t = lambda list1 : (tuple(list1))
print((t([1,2,3,4,5,6])))