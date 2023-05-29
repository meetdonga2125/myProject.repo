<<<<<<< HEAD
# Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.




a = input("Enter a value: ")

leng = len(a)

if leng>2:
    b = a[:2]
    c = a[-2:]
    a = b + c
    print(a)

else:
=======
# Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.




a = input("Enter a value: ")

leng = len(a)

if leng>2:
    b = a[:2]
    c = a[-2:]
    a = b + c
    print(a)

else:
>>>>>>> c8d5258a8ce22b04f2afe5237fdbd3e2eb85f9e0
    print(" ")        