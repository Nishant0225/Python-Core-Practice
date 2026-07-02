# ==========================================
# Encapsulation in Python
# ==========================================

# Definition:
# Encapsulation is the process of wrapping data (variables)
# and methods (functions) into a single unit called a class.

# It helps:
# • Keep related data and methods together.
# • Protect data from unauthorized access.
# • Improve security and maintainability.
# • Control how data is accessed or modified.

# Instance Variables:
# Variables created using self inside the constructor.
# Every object gets its own copy of instance variables.

# Syntax:
# self.variable_name = value

class Person:

    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input
        
        p1=Person('Nishant','India')
        p2=Person('Parth','Bharat')
    
        print(p1.name)