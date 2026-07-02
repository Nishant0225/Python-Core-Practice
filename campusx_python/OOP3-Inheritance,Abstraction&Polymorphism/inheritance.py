# ==========================================
# Inheritance in Python
# ==========================================

# Definition:
# Inheritance is an OOP concept in which one class
# acquires the properties (attributes) and methods
# of another class.

# It represents an "IS-A" relationship.

# Advantages:
# • Code Reusability
# • Reduces Code Duplication
# • Easy Maintenance
# • Extends Existing Classes

# Syntax:
# class Parent:
#     ...

# class Child(Parent):
#     ...


class User:
    def __init__(self):
        self.name='Nishant'
        self.gender='Male'
    
    def login(self):
        print('Login')


class Student(User):
    def __init__(self):
        self.rollno=100
    
    def enroll(self):
        print('Enroll in the cource')

u=User()
s=Student()

print(u.name)
print(s.rollno)
s.login()
s.enroll()


# ==========================================
# Basic Inheritance in Python
# ==========================================

# Definition:
# Inheritance is an OOP concept in which one class
# acquires the properties (attributes) and methods
# of another class.

# It represents an IS-A relationship.

# ==========================================
# Parent Class
# ==========================================

class Phone:

    # Constructor
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")

        self.price = price
        self.brand = brand
        self.camera = camera

    # Method
    def buy(self):
        print("Buying a Phone")


# ==========================================
# Child Class
# ==========================================

class SmartPhone(Phone):
    pass


# ==========================================
# Creating Object
# ==========================================

s = SmartPhone(20000, "Apple", 13)

# Calling Parent Method
s.buy()

# Accessing Parent Attributes
print("Brand  :", s.brand)
print("Price  :", s.price)
print("Camera :", s.camera)