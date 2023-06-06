# Write a Python program to find the highest 3 values in a dictionary

# Python program to demonstrate
# finding 3 highest values in a Dictionary

# Initial Dictionary
my_dict = {'A': 67, 'B': 23, 'C': 45,
		'D': 56, 'E': 12, 'F': 69}

print("Initial Dictionary:")
print(my_dict, "\n")

print("Dictionary with 3 highest values:")
print("Keys: Values")

x=list(my_dict.values())
d=dict()
x.sort(reverse=True)
# print(x)
x=x[:3]
for i in x:
    for j in my_dict.keys():
        if(my_dict[j] == i):
            print(f'{str(j)} : {my_dict[j]}')
