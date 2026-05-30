# ==========================
# TYPE CONVERSION IN PYTHON
# ==========================

# --------------------------
# Implicit Type Conversion
# --------------------------
# Python automatically converts int to float during arithmetic operations

a = 5
b = 2.5

c = a + b

print("Implicit Type Conversion:")
print(c)
print(type(c))


# --------------------------
# Explicit Type Conversion
# --------------------------
# Programmer manually converts one data type to another

a = "10"

b = int(a)

print("\nExplicit Type Conversion:")
print(b)
print(type(b))


# --------------------------
# int() Conversion
# --------------------------
# Converts values to integers

print("\nint() Conversion:")
print(int(10.8))
print(int("25"))


# --------------------------
# float() Conversion
# --------------------------
# Converts values to floating-point numbers

print("\nfloat() Conversion:")
print(float(10))
print(float("25"))


# --------------------------
# str() Conversion
# --------------------------
# Converts values to strings

a = 100

print("\nstr() Conversion:")
print(str(a))
print(type(str(a)))


# --------------------------
# bool() Conversion
# --------------------------
# Converts values to Boolean (True/False)

print("\nbool() Conversion:")
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Hello"))


# --------------------------
# list() Conversion
# --------------------------
# Converts an iterable into a list

print("\nlist() Conversion:")
print(list("Python"))


# --------------------------
# tuple() Conversion
# --------------------------
# Converts an iterable into a tuple

print("\ntuple() Conversion:")
print(tuple([1, 2, 3]))


# --------------------------
# set() Conversion
# --------------------------
# Converts an iterable into a set
# Duplicate values are removed

print("\nset() Conversion:")
print(set([1, 2, 2, 3, 3]))


# --------------------------
# Practical Examples
# --------------------------

# String to Integer Conversion
print("\nString to Integer:")
print(int("10") + 5)

# Integer to String Conversion
age = 22

print("\nInteger to String:")
print("Age: " + str(age))