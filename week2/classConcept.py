"""
All the methods of a class, including __init__, have the first parameter as self
The self keyword is used to represent an instance (object) of the given class. 
In this case, the two Cat objects cat1 and cat2 have their own name and age attributes. 
If there was no self argument, the same class couldn't hold the information for both these objects.

since the class is just a blueprint, self allows access to the attributes and methods of each object in python. 
This allows each object to have its own attributes and methods. Thus, even long before creating these objects, 
we reference the objects as self while defining the class.
"""

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

cat1 = Cat('Andy', 2)
cat2 = Cat('Phoebe', 3)
print(cat1.info())
print(cat2.make_sound())
