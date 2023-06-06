# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']}
# Expected Output:
# ac ad bc bd



my_dict= {'1':['a', 'b'], '2':['c', 'd']}
my_list= list(my_dict.values())
for i in my_list[0]:
    for j in my_list[1]:
        print(i+j)
        
        
# for i in range(1,3):
#     for j in range(11):
#         print(i*j)        