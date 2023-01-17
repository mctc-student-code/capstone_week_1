"""
Classes in Python - OOP

getter and setter methods are not common in Python - like it is in Java and C#

every method in the class should have the self attribute as the first parameter

"""

class Student: 
    # this method atleast needs one argument - self, other required arguments for the class can be set as well
    def __init__(self, name, school_id, gpa): # self is like this keyword in Java and refers to the object being initialized
        self.name = name # name of the student, instance variable
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self): # similar to toString() method in Java
        return f'Student name = {self.name}, ID: {self.school_id}, GPA: {self.gpa}'

alex = Student('Alex', 'abcdef', 3.4)
print(alex.name)
print(alex.school_id)
print(alex) # calls the str method.

sam = Student('Sam', 'qwerty',3.9)
sam.gpa = 4 # changing the gpa
print(sam)

