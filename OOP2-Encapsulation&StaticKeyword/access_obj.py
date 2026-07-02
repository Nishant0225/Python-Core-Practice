# ==========================================
# Example: Class with a Method
# ==========================================

# Definition:
# A method is a function defined inside a class.
# It is used to perform operations on the object's data.

class Person:

    # Parameterized Constructor
    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input

    # Method
    def greet(self):

        if self.country.lower() == "india":
            print("Namaste", self.name)
        else:
            print("Hello", self.name)


# Creating Objects
p1 = Person("Nishant", "India")
p2 = Person("John", "USA")

# Calling Methods
p1.greet()
p2.greet()

# Output:
# Namaste Nishant
# Hello John

# attribute creation from outside
Person.gender='male'

Person.gender