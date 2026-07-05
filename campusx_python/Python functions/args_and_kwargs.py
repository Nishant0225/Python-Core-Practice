# ==========================================
# *args IN PYTHON
# ==========================================

# *args allows a function to accept
# any number of positional arguments.

# All arguments are stored as a tuple.

def multiply(*args):
    product = 1

    for i in args:
        product = product * i

    return product

a = multiply(1, 2, 3, 4, 5, 6)

print(a)

# Output:
# 720

# ==========================================
# **kwargs IN PYTHON
# ==========================================

# **kwargs allows a function to accept
# any number of keyword arguments.

# Keyword arguments are passed as
# key=value pairs.

# All keyword arguments are stored
# as a dictionary.

def display(**kwargs):

    for key, value in kwargs.items():
        print(key, "->", value)

display(
    name="Nishant",
    age=22,
    city="Nagpur"
)

# Output:
# name -> Nishant
# age -> 22
# city -> Nagpur