# ==========================================
# NESTED FUNCTIONS IN PYTHON
# ==========================================

# A function defined inside another function
# is called a Nested Function.

# Syntax:
# def outer():
#     def inner():
#         pass

# ------------------------------------------
# BASIC EXAMPLE
# ------------------------------------------

def outer():

    def inner():
        print("Inside Inner Function")

    print("Inside Outer Function")
    inner()

outer()

# Output:
# Inside Outer Function
# Inside Inner Function

# ------------------------------------------
# NESTED FUNCTION EXAMPLE
# ------------------------------------------

def g(x):

    def h():
        x = "abc"
        print("Inside h(): x =", x)

    x = x + 1

    print("Inside g(): x =", x)

    h()

    return x

x = 3

z = g(x)

print("Global x =", x)
print("Returned value =", z)

# Output:
# Inside g(): x = 4
# Inside h(): x = abc
# Global x = 3
# Returned value = 4

# ------------------------------------------
# ACCESSING OUTER VARIABLE
# ------------------------------------------

def outer():

    x = 10

    def inner():
        print("Value of x =", x)

    inner()

outer()

# Output:
# Value of x = 10

# Inner function can access variables
# of the outer function.

# ------------------------------------------
# RETURNING A NESTED FUNCTION
# ------------------------------------------

def outer():

    def inner():
        print("Hello from Inner Function")

    return inner

func = outer()

func()

# Output:
# Hello from Inner Function

# ------------------------------------------
# USING nonlocal KEYWORD
# ------------------------------------------

def outer():

    x = 10

    def inner():
        nonlocal x
        x = 20
        print("Inner x =", x)

    inner()

    print("Outer x =", x)

outer()

# Output:
# Inner x = 20
# Outer x = 20

# nonlocal is used to modify a variable
# from the enclosing (outer) function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                