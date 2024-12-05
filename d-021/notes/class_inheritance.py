"""
-=< 100 Days of Python >=-
-=[ Day 021 ]=-
"""
"""
L.153 - Class Inheritance

Class inheritance is a feature of Object-Oriented Programming that allows a
new class to be created based on one that already exists, such that the
resulting 'child' class "inherits" all of the methods and attributes from the
'parent' class. A child class is therefore typically more specific in it's
purpose than it's parent class, whilst extending the inherited functionality
by adding new methods etc. When a method or attribute with the same name
exists in a child class it will override that of the parent on any instance
of the child class. Inheritance can also be applied over multiple levels,
meaning that it is possible to create a child from a class that is itself a
child of another class, creating a "Family Tree" type hierarchy to the path of
inheritance.

[NOTE: I believe the use of the terms as a 'child' and 'parent' class conveys
the nature of inheritance better than calling it a "subclass", since this can
imply a subset of features (i.e. methods and attributes), which is inaccurate.
However a child class can perhaps be though of as applying to a subset of the
Objects for which the Parent class applies.]

Let's look at an example to demonstrate:
"""
# pylint: disable=missing-class-docstring, missing-function-docstring
# pylint: disable=too-few-public-methods


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale...")


class Fish(Animal):
    def __init__(self, fresh_or_salt):
        super().__init__()
        self.water_type = fresh_or_salt

    def swim(self):
        print("Moving in/under water.")

    # Here we override a method inherited from the 'parent' (base) class
    def breathe(self):
        super().breathe()
        print("...using gills")


pogo = Animal()
pogo.breathe()

dory = Fish("Salt")
dory.breathe()
