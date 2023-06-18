# Explain Inheritance in Python with an example? What is init? Or What
# Is A Constructor In Python?


#---------------------------------------------------------------------------------#

#--------------------------------Inheritance--------------------------------------#

# Object of one classs can aquire the properties of another class it's called inheritance

# Creating a new class from an existing class it's called Inheritance.........


# parent class, super class, Master class
# child class, sub class, inherited class, aquire class.................

# Single level Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hirarchical Inheritance
# Hybrid Indheritance   


# Single level Inheritance:

class A:
    def getA(self,a):   
        self.a = a
    def putA(self):
        print("A : ", self.a)
class B(A):
    def getB(self,b):
        self.b = b 
    def putB(self):
        print("B : ", self.b)
        
        
b1 = B()
b1.getA(10)
b1.getB(20)
b1.putA()
b1.putB()                        
        
# Multilevel Inheritance: It makes only one object.


class A:
    def getA(self,a):   
        self.a = a
    def putA(self):
        print("A : ", self.a)
class B(A):
    def getB(self,b):
        self.b = b 
    def putB(self):
        print("B : ", self.b)
class C(B):
    def getC(self,c):
        self.c = c 
    def putC(self):
        print("C : ", self.c)            
        
        
b1 = C()
b1.getA(10)
b1.getB(20)
b1.getC(30)
b1.putA()
b1.putB()
b1.putC() 

print()


# Multiple Inheritance:   It makes only one object.


class A:
    def getA(self,a):   
        self.a = a
    def putA(self):
        print("A : ", self.a)
class B:
    def getB(self,b):
        self.b = b 
    def putB(self):
        print("B : ", self.b)
class C(A,B):
    def getC(self,c):
        self.c = c 
    def putC(self):
        print("C : ", self.c)            
        
        
b1 = C()
b1.getA(10)
b1.getB(20)
b1.getC(30)
b1.putA()
b1.putB() 
b1.putC()

print()

# Hirachichal Inheritance: It makes three object...........So rarely it is used by user

class A:
    def getA(self,a):   
        self.a = a
    def putA(self):
        print("A : ", self.a)
class B(A):
    def getB(self,b):
        self.b = b 
    def putB(self):
        print("B : ", self.b)
class C(A):
    def getC(self,c):
        self.c = c 
    def putC(self):
        print("C : ", self.c)
class D(A):
    def getD(self,d):
        self.d = d 
    def putD(self):
        print("D : ", self.d)                    
        
        
b1 = B()
c1 = C()
d1 = D()
b1.getA(10)
c1.getA(50)
b1.getB(20)
c1.getC(30)
d1.getD(40)
b1.putA()
b1.putB()
c1.putC() 
d1.putD()
c1.putA()

print()

# Hybrid Inheritance:  We can make only one object. It is mostly used inheritance.

class A:
    def getA(self,a):   
        self.a = a
    def putA(self):
        print("A : ", self.a)
class B(A):
    def getB(self,b):
        self.b = b 
    def putB(self):
        print("B : ", self.b)
class C(A):
    def getC(self,c):
        self.c = c 
    def putC(self):
        print("C : ", self.c)
class D(B,C):
    def getD(self,d):
        self.d = d 
    def putD(self):
        print("D : ", self.d)   


d1 = D()

d1.getA(10)
d1.getB(20)
d1.getC(30)
d1.getD(40)

d1.putA()        
d1.putB()        
d1.putC()        
d1.putD()   



# The Python __init__ Method 
# The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object. Now let us define a class and create some objects using the self and __init__ method.     


# Here, The Dog class is defined with two attributes:

# attr1 is a class attribute set to the value “mammal”. Class attributes are shared by all instances of the class.
# __init__ is a special method (constructor) that initializes an instance of the Dog class. It takes two parameters: self (referring to the instance being created) and name (representing the name of the dog). The name parameter is used to assign a name attribute to each instance of Dog.
# The speak method is defined within the Dog class. This method prints a string that includes the name of the dog instance.
# The driver code starts by creating two instances of the Dog class: Dog1 and Dog2. The __init__ method is called for each instance to initialize their name attributes with the provided names. The speak method is called in both instances (Dog1.speak() and Dog2.speak()), causing each dog to print a statement with its name.


class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name
		
	def speak(self):
		print(f'My dog name is {self.name}')


# Object instantiation
Dog1 = Dog("Rodger")
Dog2 = Dog("Tommy")

# Accessing class methods
Dog1.speak()
Dog2.speak()

