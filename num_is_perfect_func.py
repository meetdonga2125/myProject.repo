# Write a Python function to check whether a number is perfect or not


   
def perfect_num(n):
    
    sum = 0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            sum += i 
    # print(sum)         
    return sum == n

print(perfect_num(9))        
print(perfect_num(21))        
print(perfect_num(256))        
print(perfect_num(6))        