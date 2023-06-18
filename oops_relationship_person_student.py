# What relationship is appropriate for Student and Person?


# In object-oriented programming (OOP) concepts, the relationship between "Student" and "Person" can be represented using the inheritance relationship type. Inheritance allows you to define a new class ("Student") based on an existing class ("Person"), inheriting its properties and behaviors.

# The appropriate relationship would be "Student" inheriting from "Person." This relationship signifies that a "Student" is a specific type of "Person" with additional attributes and behaviors specific to being a student. By inheriting from "Person," the "Student" class can reuse the common attributes and behaviors defined in the "Person" class, such as name, age, and address.

# Here's an example in Python syntax to illustrate the relationship:


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f'Hello My name is {self.name} and I am {self.age} old. and curretly I am living in {self.address}.')


class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f'Now i am student. and my Student ID is {self.student_id}')


# Creating objects and accessing attributes
person = Person("John Doe", 25, "123 Main St")
person.display_info()

student1 = Student("Jane Smith", 20, "456 Elm St", "S123456")
student1.display_info()

student2 = Student("Kartik", "23", "Gandhinagar", 'S456789')
student2.display_info()

# In this example, the "Student" class inherits from the "Person" class using the class Student(Person) statement. The "Student" class has an additional attribute, "student_id," which is specific to students. By using the super().__init__() method in the "Student" class's constructor, the "name," "age," and "address" attributes from the "Person" class are also initialized.

# The "display_info" method is overridden in the "Student" class to add the "student_id" attribute while still displaying the information inherited from the "Person" class using super().display_info().

# By using inheritance, you can model the "is-a" relationship between "Student" and "Person," indicating that a student is a specialized type of person.
