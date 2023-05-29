#  Write a Python function that takes a list and returns a new list with unique
# elements of the first list


def unique_list(list1):
    list2 = set(list1)
    
    unique1 =list(list2)
    for i in unique1:
        print(i)
    
unique_list([10,20,30,40,10,30,50])    



def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 
