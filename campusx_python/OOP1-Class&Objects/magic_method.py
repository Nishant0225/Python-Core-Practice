# ==========================================
# Magic (Dunder) Methods in Python
# ==========================================

# Definition:
# Magic methods (also called Dunder methods) are special methods
# whose names start and end with double underscores (__).
# Python automatically calls these methods to perform specific tasks.

# Syntax:
# def __method_name__(self):
#     pass

# Common Magic Methods:

# 1. __init__()
# Automatically called when an object is created.
# Used to initialize instance variables.

# 2. __str__()
# Returns a user-friendly string representation of an object.
# Called automatically by print(object).

# 3. __repr__()
# Returns the official string representation of an object.
# Mainly used for debugging.

# 4. __len__()
# Returns the length of an object.
# Called by len(object).

# 5. __name__
# A special built-in variable.
# Stores the name of the current module.
# If the file is run directly, its value is "__main__".

# Example:
# if __name__ == "__main__":
#     print("Program is running directly.")

# 6. __file__
# Stores the path of the current Python file.

# 7. __doc__
# Stores the documentation (docstring) of a class, function, or module.

# 8. __dict__
# Returns a dictionary containing an object's attributes.

# 9. __module__
# Returns the name of the module in which the class is defined.

# 10. __class__
# Returns the class of an object.

# Note:
# __path__ is NOT a commonly used magic method.
# It is a special attribute available only in Python packages.
# It stores the package search path and is not available for normal classes.

# Key Points:
# • Magic methods begin and end with double underscores (__).
# • They are automatically called by Python.
# • They allow us to customize the behavior of objects.
# • __init__() is the most commonly used magic method.

# Memory Trick:
# Dunder = Double UNDERscore
# __init__ → Initialize object
# __str__ → String representation
# __len__ → Length of object
# __name__ → Name of current module

# Interview Question:
# Q. What are magic (dunder) methods?
# A. Magic methods are special methods with double underscores that
# Python automatically invokes to perform predefined operations.