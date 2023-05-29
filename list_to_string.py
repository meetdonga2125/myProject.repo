# Write a Python program to convert a list of characters into a string.

l = ["Apple", "Pinaple", "Banana", "Grapes", "Oranges", "Cherry"]

list_string = " ".join(l)
print(list_string)







#Method-2---------------------------------------------------------------

# Python program to convert a list
# of character

def convert(s):

	# initialization of string to ""
	new = ""

	# traverse in the string
	for x in s:
		new += x

	# return string
	return new
	
	
# driver code
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))
