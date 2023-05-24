# What are negative indexes and why are they used?


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

#eg.
#       012345678901234567  ---> Positive Index
lang = "Python Programming"
#       876543210987654321  --->  Negative index..................     
print(lang[-1])
print(lang[-6:-1])     # It inculde -6 to -2 and it does't include last index..............
print(lang[:-1])
print(lang[-2:])