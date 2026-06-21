# ==========================================
# FUNCTIONS ARE FIRST-CLASS CITIZENS
# ==========================================

# In Python, functions are treated like
# any other object (int, string, list, etc.)

# This means functions can:
# 1. Have a type and id
# 2. Be assigned to variables
# 3. Be deleted
# 4. Be stored in data structures
# 5. Be passed as arguments
# 6. Be returned from other functions

# ------------------------------------------
# 1. TYPE AND ID OF A FUNCTION
# ------------------------------------------

def square(x):
    return x * x

print(type(square))
print(id(square))

# Output:
# <class 'function'>
# (Memory address will vary)

# ------------------------------------------
# 2. REASSIGNING A FUNCTION
# ------------------------------------------

def greet():
    print("Hello")

a = greet

a()

# Output:
# Hello

# Both a and greet refer to the same function.

# ==========================================
# 3. DELETING A FUNCTION
# ==========================================

def greet():
    print("Hello")

del greet

# greet()

# Output:
# NameError:
# name 'greet' is not defined

# ==========================================
# 4. STORING FUNCTIONS
# ==========================================

def square(x):
    return x * x

def cube(x):
    return x * x * x

functions = [square, cube]

print(functions[0](5))
print(functions[1](5))

# Output:
# 25
# 125

# Functions can be stored in lists,
# tuples, dictionaries, etc.

# ==========================================
# 5. PASSING FUNCTION AS ARGUMENT
# ==========================================

def square(x):
    return x * x

def operate(func, value):
    return func(value)

print(operate(square, 5))

# Output:
# 25

# Here square is passed as an argument.


# ==========================================
# 6. RETURNING A FUNCTION
# ==========================================

def outer():

    def inner():
        print("Hello from Inner Function")

    return inner

func = outer()

func()

# Output:
# Hello from Inner Function

# First-Class Citizen

# A function is called a First-Class Citizen
# if it can be treated like any other object.

# Functions Can:

# ✔ Have a type and id
# ✔ Be assigned to variables
# ✔ Be deleted
# ✔ Be stored in data structures
# ✔ Be passed as arguments
# ✔ Be returned from functions