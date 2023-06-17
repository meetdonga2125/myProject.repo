#  When is the finally block executed?

#Exception Handling, try and except in Python In programming, there may be some situation in which the current method ends up while handling some exceptions. But the method may require some additional steps before its termination, like closing a file or a network and so on. So, in order to handle these situations, Python provides a keyword finally, which is always executed after try and except blocks. The finally block always executes after normal termination of try block or after try block terminates due to some exception.


# Python program to demonstrate finally

# No exception Exception raised in try block
try:
	k = 5//0 # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")
	
finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')



#------------------------------------------------------------------


# Python program to demonstrate finally

try:
	k = 5//1 # No exception raised
	print(k)

# intends to handle zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")
	
finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')
 
 
#----------------------------------------------------------------


# Python program to demonstrate finally

# Exception is not handled
try:
	k = 5//0 # exception raised
	print(k)
	
finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')
 
