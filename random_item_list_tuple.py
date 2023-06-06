# How can you pick a random item from a list or tuple?

import random

my_list = [10,20,"Meet", 1.2, 0, False, None, "cricket", 50]
my_tuple  = (10,20,30,40,10,1.2,False)

random_list = random.choice(my_list)
print(random_list)

random_tuple = random.choice(my_tuple)
print(random_tuple)