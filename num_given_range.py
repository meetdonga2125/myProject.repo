# Write a Python function to check whether a number is in a given range


def myFunc(a):
    
    for i in range(20):
        if i==a:
            print(i, "Yes I am present in given range!!")
            break
    else:
        print("I am Out of range")  
             
            
myFunc(15)   
myFunc(21)         
