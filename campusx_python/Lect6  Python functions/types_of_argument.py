# ==========================================
# TYPES OF ARGUMENTS IN PYTHON
# ==========================================

# 1. Default Argument
# 2. Positional Argument
# 3. Keyword Argument

# ==========================================
# 1. DEFAULT ARGUMENT
# ==========================================

def power(a, b=2):
    return a ** b

print(power(3))
print(power(3, 3))

# Output:
# 9
# 27

# If b is not provided,
# default value (2) is used.

# ==========================================
# 2. POSITIONAL ARGUMENT
# ==========================================

def subtract(a, b):
    return a - b

print(subtract(10, 5))

# Output:
# 5

# Arguments are assigned according
# to their position.

# ==========================================
# 3. KEYWORD ARGUMENT
# ==========================================

def student(name, age):
    print("Name:", name)
    print("Age :", age)

student(age=22, name="Nishant")

# Output:
# Name: Nishant
# Age : 22

# Arguments are assigned using
# parameter names.

# ==========================================
# COMBINED EXAMPLE
# ==========================================

def power(a, b=2):
    return a ** b

# Default Argument
print(power(5))

# Positional Argument
print(power(5, 3))

# Keyword Argument
print(power(b=4, a=2))

# Output:
# 25
# 125
# 16


# ==========================================
# PARAMETERS VS ARGUMENTS
# ==========================================

# Parameter:
# Variables defined in the function definition.

# Argument:
# Actual values passed during the function call.

def add(a, b):      # a and b are PARAMETERS
    return a + b

print(add(10, 20))  # 10 and 20 are ARGUMENTS

# Output:
# 30