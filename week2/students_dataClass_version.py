"""
Part 3
- new concept
Python's dataclass remove a lot of the
boilerplate* from class definitions
• Give you __init__, __str__ methods for free

boilerplate - Standard code that is included in many
places and is usually very boring to write,
e.g. constructors that simply set values, get
and set methods, toString/__str__
methods...

"""

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: str
    gpa: float
    # data classes have methods defined already and we don't need to explicitly define it like in regular traditional class
    # you can override the toString methods
    def __str__(self): # similar to toString() method in Java
        return f'Student name = {self.name}, ID: {self.college_id}, GPA: {self.gpa}'


def main():
    alex = Student('Alex', 'abcdef', 3.4)
    print(alex.name)
    print(alex.college_id)
    print(alex) # calls the str method.

    sam = Student('Sam', 'qwerty', 3.9)
    sam.gpa = 4 # changing the gpa
    print(sam)

# if this file is imported into other file, __name__ is set to name of the file where it is imported and hence main() 
# method is not called, but when the program is running from command prompt, __name__ is set to __main__ and main()
# is called.
if __name__ == '__main__': 
    main()