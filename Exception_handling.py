# Explain Exception handling? What is an Error in Python?


#Errors are problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which change the normal flow of the program. 


# An abnormal situation that arises durinng the runtime of program is called the exception

#Exceptions: Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program

# initialize the amount variable
# marks = 10000

# # perform division with 0
# a = marks / 0
# print(a)


# 1) TypeError: This exception is raised when an operation or function is applied to an object of the wrong type. Here’s an example:

# x = 5
# y = "hello"
# z = x + y # Raises a TypeError: unsupported operand type(s) for +: 'int' and 'str'


#try catch block resolve it

x = 5
y = "hello"
try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")
 
print("Hello world") 


#Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.


#First, the try clause is executed i.e. the code between try.
# If there is no exception, then only the try clause will run, except clause is finished.
# If any exception occurs, the try clause will be skipped and except clause will run.
# If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
# A try statement can have more than one except clause


