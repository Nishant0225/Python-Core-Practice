# ==========================================
# Reference Variable in Python
# ==========================================

# Definition:
# A reference variable stores the reference (memory address)
# of an object.
# It is used to access the object's attributes and methods.

# Syntax:
# reference_variable = ClassName()

class Student:

    # Constructor
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# Outside the class --> Function
def greet(student):      # student is a reference variable
    print("Hi my name is", student.name, "and I am a", student.gender)

    # Creating a new object
    p1 = Student("Kumar", "Male")
    return p1


# Creating an object
s = Student("Nishant", "Male")

# Passing the reference variable to the function
x = greet(s)

# x stores the reference of the object returned by greet()
print(x.name)
print(x.gender)