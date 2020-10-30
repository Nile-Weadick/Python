"""
Description: Create a class in Python 3 named Animal that has specified attributes and methods.

Purpose: The purpose of this challenge is to provide experience creating a class and working with OO concepts in Python 3.

Requirements:

Write a class in Python 3 named Animal that has the following attributes and methods and is saved in the file Animal.py.

Attributes
animal_type is a hidden attribute used to indicate the animal’s type. For example: gecko, walrus, tiger, etc.

name is a hidden attribute used to indicate the animal’s name.

mood is a hidden attribute used to indicate the animal’s mood. For example: happy, hungry, or sleepy.

Methods
init is to define the three attributes above and assign their default values.
"""

class Animal:
    #init is to define the three attributes type, name, mood
    def _init_(self,spec,name,mood):
        self.spec = spec
        self.name = name
        self.mood = mood
    
    # set methods to asign value to object
    def set_spec(self, spec):
        self.spec = spec

    def set_name(self, name):
        self.name = name

    def set_mood(self, mood):
        self.mood = mood

    #get methods to return the objects attributes
    def get_spec(self):
        return self.spec

    def get_name(self):
        return self.name

    def get_mood(self):
        return self.mood

