# How can you pick a random item from a range?

import random

list1 = []
for i in range(10):
    num = random.randint(1,100)
    list1.append(num)

print(list1)    