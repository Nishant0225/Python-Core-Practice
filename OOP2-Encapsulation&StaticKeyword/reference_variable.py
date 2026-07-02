# ==========================================
# Reference Variable in Python
# ==========================================

# Definition:
# A reference variable is a variable that stores the reference
# (memory address) of an object.
# It is used to access the object's data and methods.

# Syntax:
# reference_variable = ClassName()

# Example:

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


# Creating an object
s1 = Student("Nishant")

# s1 is a reference variable
print(s1)

# Accessing instance variable
print(s1.name)

# Calling method using reference variable
s1.display()

# Output:
# <__main__.Student object at 0x...>
# Name: Tanvi
# Name: Tanvi