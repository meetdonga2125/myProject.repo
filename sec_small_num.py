# Write a Python program to find the second smallest number in a list


l = [10,20,30,42,2,52,63,215,458,521,21,20,65,42,1]
l1 = set(l)

# convert l1 into list
l2 = list(l1)
# Find a minimum number from l2
l3 = min(l2)
# Remove min number from l2
l4 = l2.remove(l3)
# sorting of l2
l2.sort()
# Now the zero index value is min number bcz first small value we removed by l4 variable 
print(l2[0])


