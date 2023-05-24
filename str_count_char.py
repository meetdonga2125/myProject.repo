# Write a Python program to count the number of characters (character
# frequency) in a string


str1 = "Python programming"
str_count = {}

for i in str1:
    if i in str_count:
        str_count[i] += 1
    else:
        str_count[i] = 1

print("Count of all characters in GeeksforGeeks is :\n "
      + str(str_count))          



