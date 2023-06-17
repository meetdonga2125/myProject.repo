#  Write python program that user to enter only odd numbers, else will
# raise an exception


num = int(input("Enter a num: "))

if num%2!=0:
    print(f'{num} is a odd number')
else:
    raise Exception(f'Sorry, {num} is not a odd number')    
            
    