# class p 
# attributes/methods/properties
# # access and using the properties and method for the parent calss


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduceyourself(self):
        print("my name is "+ self.name)
        print("my age is "+str(self.age))

class Teacher(Person):
    def stateprofession(Self):
        print("I am a teacher")

author = Teacher("Rakesh",25)
author.introduceyourself()
author.stateprofession()