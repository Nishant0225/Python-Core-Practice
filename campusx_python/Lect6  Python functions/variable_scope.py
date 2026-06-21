# ==========================================
# VARIABLE SCOPE IN PYTHON
# ==========================================

# Scope refers to the region where a variable
# can be accessed.

# Types:
# 1. Global Scope
# 2. Local Scope

# ==========================================
# GLOBAL VARIABLE
# ==========================================

x = 5

def g(y):
    print(x)
    print(x + 1)

g(x)

print(x)

# Output:
# 5
# 6
# 5

# x is a global variable because it is
# declared outside the function.

# ==========================================
# LOCAL VARIABLE
# ==========================================

def f():
    x = 10
    print(x)

f()

# print(x)
# Error if x is not defined globally

# x is local to the function.

# ==========================================
# GLOBAL AND LOCAL VARIABLE
# ==========================================

x = 5

def display():
    x = 10
    print("Local x =", x)

display()

print("Global x =", x)

# Output:
# Local x = 10
# Global x = 5

# ==========================================
# MODIFYING GLOBAL VARIABLE
# ==========================================

x = 5

def change():
    global x
    x = 20

change()

print(x)

# Output:
# 20

# global keyword is used to modify
# a global variable inside a function.