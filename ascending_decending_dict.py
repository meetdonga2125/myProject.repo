# Write a Python script to sort (ascending and descending) a dictionary by
# value


myDict = {'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}

myvalues = list(myDict.values())
myvalues.sort()

print(myvalues)
print(myDict.items())


#1. sort dictionary by value Ascending
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
a = sorted(d.items(), key=lambda x: x[1])
print(a)

#2. Sort dictionary by value descending
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
a = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(a)






