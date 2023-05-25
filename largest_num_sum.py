# Write a Python function to get the largest number, smallest num and sum
# of all from a list.


def max_min(list1):
    # a = [10,20,54,2,65,89,357,25]
    list1.sort()
    sum = 0
    for i in list1:
        if i==list1[0]:
            print(i, "is min")
        elif i==list1[-1]:
            print(i, "Is Max")
                        
a = [10,20,56,85,98,65,58,256,54,358,256]   
max_min(a)    


def sum_list(list1):
    sum = 0
    for i in list1:
        sum += i
    print(sum)    
    
    
result = [10,256,24,56,65,985,2561,2,2145,254,19]    
sum_list(result)

