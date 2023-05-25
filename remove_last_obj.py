# How will you remove last object from a list?
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?


# By using pop() method we can remove the last element by default 
# And using remove() method we can remove an element by enter a last element inside a remove method


list1 = [2, 33, 222, 14, 25]
list1.pop()
print(list1)

# list1.remove(14)
# print(list1)

# By using specific location

print(list1.pop(-1))           # It can be removed last element of list using indexing........................
print(list1)