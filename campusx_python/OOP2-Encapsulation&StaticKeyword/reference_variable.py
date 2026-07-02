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

    def __init__(self, name,gender):
        self.name = name 
        self.gender=gender
# Outside the class -->Function 
def greet(Student):
    print('Hi my name is ',Student.name,'and I am a',Student.gender)
    
s=Student('Nishant','Male')
p=greet(s)