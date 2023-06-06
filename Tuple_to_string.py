# Write a Python program to convert a tuple to a string


a = ("Python", "Java", "Javascript", "Node", "Django", "React")

convert_string = " ".join(a)
print(convert_string)


b = ["P", "y", "t", "h", "o", "n"]

convert_string2 = "".join(b)
print(convert_string2)


#Methoc-d-------------------------------------------------------------


# Python3 code to convert a tuple
# into a string using a for loop


def convertTuple(tup):
		# initialize an empty string
	str = ''
	for item in tup:
		str = str + item
	return str


# Driver code
tuple = ("D","j","a","n","g","o")
str = convertTuple(tuple)
print(str)



