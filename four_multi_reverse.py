# Write a Python function to reverses a string if its length is a multiple of 4.


a = input("Enter a value: ")
b = len(a)
# print(b)

if b%4==0:
    print(a[::-1])                   #reverse a string
else:
    print(a)    
    