# Write a Python function to insert a string in the middle of a string


# Python3 code to demonstrate working of
# Add Phrase in middle of String
# Using insert()


# initializing string
test_str = 'The quick brown fox jumps over the lazy dog'
# printing original string
print("The original string is : " + str(test_str))
test=test_str.split()
# initializing mid string
mid_str = "best"
# finding middle word
mid_pos = len(test) // 2
test.insert(mid_pos,mid_str)
# printing result
print("Formulated String : " + str(" ".join(test)))


a = "Meet dongaa"
b = len(a)//2
print(b)
