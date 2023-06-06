# Why Do You Use the Zip () Method in Python

# Python zip() with lists
# In Python, the zip() function is used to combine two or more lists (or any other iterables) into a single iterable, where elements from corresponding positions are paired together. The resulting iterable contains tuples, where the first element from each list is paired together, the second element from each list is paired together, and so on.


name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]

# using zip() to map values
mapped = zip(name, roll_no)

print(list(mapped))


