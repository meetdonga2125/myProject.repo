#A Function which have no name it's called Anonymous Function.

# Python code to illustrate the cube of a number
# using lambda function
#Eg.1------------------------------------------------------------------------------
def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))



#Example-2---------------------------------------------------------------------------

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
	print(item())




# def is_even(list1):
#     for i in list1:
#         print(i*10)
        
# is_even([1,2,3,4]) 
 


#example-3------------------------------------------------------------------------------

str1 = "Tops Technologies"
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))


def rev_upper1(str2):
    return str2.upper()[::-1]

print(rev_upper1(str1)) 

sum = lambda a,b : a+b
print(sum(45,65))


#eg.4------------------------------------------------------------------------------------

square = lambda n : (i*i for i in range(n)) 
print(list(square(15))) 


#eg.5-------------------------------------------------------------------------------------

# python code to find maximum of two numbers

a = int(input("Enter a value of a: "))
b = int(input("Enter a value of b: "))
maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} is a maximum number')


#eg.6------------------------------------------------------------------------------------


x = lambda list1 : (list1[0])

print(x([10,20,30]))


#eg.7------------------------------------------------------------------------------------

t = lambda list1 : (tuple(list1))
print((t([1,2,3,4,5,6])))


#eg.8-------------------------------------------------------------------------------------




starts_with = lambda x: True if x.startswith('I') else False
print(starts_with("India"))

starts_with = lambda x: True if x.startswith('G') else False
print(starts_with("England"))


l = lambda y : True if y.startswith("a") else False
print(l("apple"))

     
    
# nums = [3,2,6,8,4,2,9]
# evens = list(filter(lambda n : n%2==0, nums))
# evens = list(filter(lambda n : n%2!=0, nums))
# print(evens)
# print(evens)   
# double = list(map(lambda n : n*2, evens))
# print(double)   


#############################################################
def square(num):   
    return num*num

num = [1,2,3,4,5]

num1 = []
for i in num:
    sqare_num = square(i)
    num1.append(sqare_num)

print(num1)    
########################   With Map Function        #############################################

list1 = list(map(square,num))
print(list1)

#######################    WIth list comprehension  #############################################

list1 = [i*i for i in num]
print(list1)


list1 = lambda list2 : (i*i for i in list2)
print(list(list1([1,2,3,4,5,6])))



##################################################################################################

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
    
mystring = ["Apple", "Mango", "Banana", "Kiwi", "Grapes", "Cherry"]        

print(list(map(splicer,mystring)))

#################################################################################################

list1 = list(map(lambda i : i*i, [1,2,3,4]))
print(list1)


##################################################################################################

list1 = ["Mango", "Banana", "Grapes", "Oranges", "Apple"]

list2 = list(map(lambda x: x[::-1], list1))
print(list2)







 
    

      
