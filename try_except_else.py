# When will the else part of try-except-else be executed?


# Else Clause
# The code enters the else block only if the try clause does not raise an exception.

# Example: Else block will execute only when no exception occurs.


# Python code to illustrate
# working of try()
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional
		# Part as Answer
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
  
	else:
		print("Yeah ! Your answer is :", result)

# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)
