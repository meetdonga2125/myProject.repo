# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.


# To create a class, use the keyword class:

class MyClass:
  x = 5

print(MyClass)

#----------------------------------------------------

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print(f"Hello my name is {self.name} and I am {self.age} old.")

p1 = Person("kishan", 24)
p1.myfunc()
