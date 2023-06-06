
# Differentiate between append () and extend () methods?



# What is Append in Python?
# Python’s append() function inserts a single element into an existing list. The element will be added to the end of the old list rather than being returned to a new list. Adds its argument as a single element to the end of a list. The length of the list increases by one. 


list_append = ["Fruits", "Vegetables", "Games", 1, 12, "Meet", "body"]
#Now using a append method
list_append.append("Python")         # It will add a Python at the end of the list...and It add only one element into the list....
print(list_append)


# What is extend() in Python? 
# Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by a number of elements in its argument.

list_extend = ["India", "Germany", "Egypt", 1 , 0.2, "Argentina", "Canada", "Antarctica"]
list_extend.extend(list_append)

# Differentiate between append () and extend () methods?



# What is Append in Python?
# Python’s append() function inserts a single element into an existing list. The element will be added to the end of the old list rather than being returned to a new list. Adds its argument as a single element to the end of a list. The length of the list increases by one. 


list_append = ["Fruits", "Vegetables", "Games", 1, 12, "Meet", "body"]
#Now using a append method
list_append.append("Python")         # It will add a Python at the end of the list...and It add only one element into the list....
print(list_append)


# What is extend() in Python? 
# Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by a number of elements in its argument.

list_extend = ["India", "Germany", "Egypt", 1 , 0.2, "Argentina", "Canada", "Antarctica"]
list_extend.extend(list_append)

print(list_extend)