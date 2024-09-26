class Person:
    def __init__ (self, name):
        self.name = name

p = Person("Nishanth")
print(p.name)

# Example 2

class Human:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Human('Rakesh', 'Kumar', 25, 'India', 'mysore')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city) 

# example method
class Human:
    def __init__(self, firstname='Rakesh', lastname='Kumar', age=25, country='India', city='Mysuru'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f"{self.firstname} {self.lastname}, Age: {self.age}, Country: {self.country}, City: {self.city}"

# Create an instance of the class
p = Human()
print(p.person_info())

# Create another instance with different attributes
p1 = Human("Nishanth", "H S", 21, "India", "Mysuru")
print(p1.person_info())

     

