# Write a Python program to check multiple keys exists in a dictionary


# Python3 code to check multiple key existence
# using comparison operator

# initializing a dictionary
sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}

# using comparison operator
print(sports.keys() >= {"geeksforgeeks", "practice"})
print(sports.keys() >= {"contribute", "ide"})

    
            