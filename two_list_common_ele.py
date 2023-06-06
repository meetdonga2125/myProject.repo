# Write a Python function that takes two lists and returns true if they have
# at least one common member.


def common_ele(a,b):
    
    for i in a:
    
      for j in b:
        
        if  i==j:
            
            return True
        
    return True    


        
                  

print(common_ele([1,2,3],[2,3,4]))        