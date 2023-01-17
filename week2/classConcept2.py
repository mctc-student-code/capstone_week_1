"""
__init__() defines three parameters but we just passed two (6 and 8). 
Similarly distance() requires one but zero arguments were passed. 
Why is Python not complaining about this argument number mismatch?
"""

class Point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5
    

p1 = Point(6,8)
print(p1.distance())

print(type(Point.distance)) # class - function
print(type(p1.distance)) # object instance - method

"""We can see that the first one is a function and the second one is a method. 
A peculiar thing about methods (in Python) is that the object itself is passed as the first argument 
to the corresponding function.
In the case of the above example, the method call p1.distance() is actually equivalent to Point.distance(p1).

Generally, when we call a method with some arguments, the corresponding class function is called by placing 
the method's object before the first argument. So, anything like obj.meth(args) becomes Class.meth(obj, args)

This is the reason the first parameter of a function in class must be the object itself. 
Writing this parameter as self is merely a convention. It is not a keyword and has no special meaning in Python. 
We could use other names (like this) but it is highly discouraged. 
Using names other than self is frowned upon by most developers and degrades the readability of the code (Readability counts).

"""

# Self can be avoided
class A(object):
    
    @staticmethod
    def stat_meth():
        print("Look no self was passed")

# @staticmethod is a function decorator that makes stat_meth() static. 
a = A()
print(a.stat_meth())

""" we can see that the implicit behavior of passing the object as the first argument was avoided while using a static method.
 All in all, static methods behave like the plain old functions (Since all the objects of a class share static methods)."""

print(type(A.stat_meth)) # class function
print(type(a.stat_meth)) # class function

"""
Many have proposed to make self a keyword in Python, like this in C++ and Java. 
This would eliminate the redundant use of explicit self from the formal parameter list in methods.
While this idea seems promising, it is not going to happen. At least not in the near future. 
The main reason is backward compatibility.
"""
# __init__() is not a constructor

"""
A closer inspection will reveal that the first parameter in __init__() is the object itself (object already exists). 
The function __init__() is called immediately after the object is created and is used to initialize it.

Technically speaking, a constructor is a method which creates the object itself. In Python, this method is __new__(). 
A common signature of this method is:

__new__(cls, *args, **kwargs)

When __new__() is called, the class itself is passed as the first argument automatically(cls).

Again, like self, cls is just a naming convention. 
Furthermore, *args and **kwargs are used to take an arbitrary number of arguments during method calls in Python.

Some important things to remember when implementing __new__() are:

__new__() is always called before __init__().
First argument is the class itself which is passed implicitly.
Always return a valid object from __new__(). Not mandatory, but its main use is to create and return an object.
"""

class Point(object):
    
    def __new__(cls,*args,**kwargs):
        print("From new")
        print(cls)
        print(args)
        print(kwargs)

        # create our object and return it
        obj = super().__new__(cls)
        return obj

    def __init__(self,x = 0,y = 0):
        print("From init")
        self.x = x
        self.y = y

p2 = Point(2,3) # check output

"""
This example illustrates that __new__() is called before __init__(). 
We can also see that the parameter cls in __new__() is the class itself (Point). 
Finally, the object is created by calling the __new__() method on object base class.

In Python, object is the base class from which all other classes are derived. 
In the above example, we have done this using super().
"""

"""
You might have seen __init__() very often but the use of __new__() is rare. 
This is because most of the time you don't need to override it. 
Generally, __init__() is used to initialize a newly created object while __new__() is used to control the way an object is created.

We can also use __new__() to initialize attributes of an object, but logically it should be inside __init__().

One practical use of __new__(), however, could be to restrict the number of objects created from a class.

Suppose we wanted a class SqPoint for creating instances to represent the four vertices of a square.
 We can inherit from our previous class Point (the second example in this article) 
 and use __new__() to implement this restriction. Here is an example to restrict a class to have only four instances.
"""

class SqPoint(Point):
    MAX_Inst = 4
    Inst_created = 0

    def __new__(cls,*args,**kwargs):
        if (cls.Inst_created >= cls.MAX_Inst):
            raise ValueError("Cannot create more objects")
        cls.Inst_created += 1
        return super().__new__(cls)

p1 = SqPoint(0,0)
p2 = SqPoint(1,0)
p3 = SqPoint(1,1)
p4 = SqPoint(0,1)

p5 = SqPoint(2,2) # ValueError since limit is 4
