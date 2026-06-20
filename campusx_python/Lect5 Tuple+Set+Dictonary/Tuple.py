# ==========================================
# TUPLES IN PYTHON
# ==========================================

# A tuple in Python is similar to a list.
# The main difference is that tuples are immutable,
# which means their elements cannot be changed after creation.

# In short, a tuple is an immutable list.

# ------------------------------------------
# CHARACTERISTICS OF TUPLES
# ------------------------------------------

# 1. Ordered
#    - Elements maintain their insertion order.

# 2. Immutable (Unchangeable)
#    - Elements cannot be added, removed, or modified.

# 3. Allows Duplicate Values
#    - Duplicate elements are allowed.

# 4. Can Store Multiple Data Types
#    - A tuple can contain integers, strings, floats, etc.

# ------------------------------------------
# CREATING A TUPLE
# ------------------------------------------

t1 = (10, 20, 30, 40)
print(t1)

# Tuple with duplicate values
t2 = (1, 2, 2, 3, 3, 4)
print(t2)

# Tuple with different data types
t3 = (1, "Python", 3.14, True)
print(t3)

# ------------------------------------------
# ACCESSING ELEMENTS
# ------------------------------------------

print(t1[0])      # First element
print(t1[-1])     # Last element

# ------------------------------------------
# IMMUTABILITY EXAMPLE
# ------------------------------------------

# t1[0] = 100
# TypeError: 'tuple' object does not support item assignment

# ------------------------------------------
# ADVANTAGES OF TUPLES
# ------------------------------------------

# 1. Faster than lists
# 2. Uses less memory
# 3. Data remains safe from accidental modification
# 4. Useful for fixed collections of data

# ------------------------------------------
# SUMMARY
# ------------------------------------------

# Tuple = Ordered + Immutable + Allows Duplicates

# ==========================================
# CREATING TUPLES IN PYTHON
# ==========================================

# Empty Tuple
t1 = ()
print(t1)

# Create a tuple with a single item
# Note: Comma (,) is mandatory for a single-element tuple
t2 = ('hello',)
print(t2)
print(type(t2))

# Homogeneous Tuple
# All elements are of the same data type
t3 = (1, 2, 3, 4)
print(t3)

# Heterogeneous Tuple
# Elements are of different data types
t4 = (1, 2.5, True, [1, 2, 3])
print(t4)

# ==========================================
# OUTPUT
# ==========================================

# ()
# ('hello',)
# <class 'tuple'>
# (1, 2, 3, 4)
# (1, 2.5, True, [1, 2, 3])

# ==========================================
# NESTED TUPLE & TYPE CONVERSION
# ==========================================

# Nested Tuple
# A tuple can contain another tuple as an element.

t5 = (1, 2, 3, (4, 5))
print(t5)

# Using Type Conversion
# The tuple() function converts an iterable into a tuple.

t6 = tuple('hello')
print(t6)

# ==========================================
# OUTPUT
# ==========================================

# (1, 2, 3, (4, 5))

# ('h', 'e', 'l', 'l', 'o')

# ==========================================
# ACCESSING TUPLE ITEMS
# ==========================================

# We can access tuple elements using:
# 1. Indexing
# 2. Slicing

t3 = (1, 2, 3, 4)

# ------------------------------------------
# INDEXING
# ------------------------------------------

# Positive Indexing
print(t3[0])   # First element
print(t3[1])   # Second element

# Negative Indexing
print(t3[-1])  # Last element
print(t3[-2])  # Second last element

# Display complete tuple
print(t3)

# ==========================================
# OUTPUT
# ==========================================

# 1
# 2
# 4
# 3
# (1, 2, 3, 4)

# ==========================================
# SLICING IN TUPLES
# ==========================================

# Slicing is used to access multiple elements
# from a tuple.

t3 = (1, 2, 3, 4, 5, 6)

# Syntax:
# tuple_name[start : end : step]

# ------------------------------------------
# BASIC SLICING
# ------------------------------------------

print(t3[0:3])    # Elements from index 0 to 2
print(t3[2:5])    # Elements from index 2 to 4
print(t3[:4])     # From beginning to index 3
print(t3[2:])     # From index 2 to end
print(t3[:])      # Complete tuple

# ------------------------------------------
# NEGATIVE SLICING
# ------------------------------------------

print(t3[-4:-1])  # Elements from -4 to -2
print(t3[-3:])    # Last three elements

# ------------------------------------------
# STEP SLICING
# ------------------------------------------

print(t3[::2])    # Every 2nd element
print(t3[1::2])   # Every 2nd element starting from index 1
print(t3[::-1])   # Reverse tuple

# ==========================================
# OUTPUT
# ==========================================

# (1, 2, 3)
# (3, 4, 5)
# (1, 2, 3, 4)
# (3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)
# (3, 4, 5)
# (4, 5, 6)
# (1, 3, 5)
# (2, 4, 6)
# (6, 5, 4, 3, 2, 1)

# ==========================================
# EDITING ITEMS IN A TUPLE
# ==========================================

# Tuples are immutable (unchangeable).
# Once a tuple is created, its elements
# cannot be modified, added, or removed.

t1 = (10, 20, 30, 40)

# Trying to change an element
# t1[0] = 100

# Output:
# TypeError: 'tuple' object does not support item assignment

# ------------------------------------------
# WORKAROUND
# ------------------------------------------

# Convert tuple to list
temp = list(t1)

# Modify the list
temp[0] = 100

# Convert back to tuple
t1 = tuple(temp)

print(t1)

# Output:
# (100, 20, 30, 40)

# ==========================================
# OPERATIONS ON TUPLES
# ==========================================

t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

# ------------------------------------------
# CONCATENATION (+)
# ------------------------------------------

# Combines two tuples

print(t1 + t2)

# Output:
# (1, 2, 3, 4, 5, 6, 7, 8)

# ------------------------------------------
# REPETITION (*)
# ------------------------------------------

# Repeats tuple elements

print(t1 * 3)

# Output:
# (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

# ------------------------------------------
# MEMBERSHIP OPERATORS
# ------------------------------------------

# in      -> Checks if an element exists
# not in  -> Checks if an element does not exist

print(2 in t1)
print(10 in t1)

print(10 not in t1)

# Output:
# True
# False
# True

# ------------------------------------------
# ITERATION
# ------------------------------------------

# Traversing a tuple using a loop

for i in t1:
    print(i)

# Output:
# 1
# 2
# 3
# 4

# ==========================================
# COMMON FUNCTIONS USED WITH TUPLES
# ==========================================

t = (1, 2, 3, 4)

# ------------------------------------------
# len()
# ------------------------------------------

# Returns the number of elements in a tuple

print(len(t))

# Output:
# 4

# ------------------------------------------
# sum()
# ------------------------------------------

# Returns the sum of all elements

print(sum(t))

# Output:
# 10

# ------------------------------------------
# min()
# ------------------------------------------

# Returns the smallest element

print(min(t))

# Output:
# 1

# ------------------------------------------
# max()
# ------------------------------------------

# Returns the largest element

print(max(t))

# Output:
# 4

# ------------------------------------------
# sorted()
# ------------------------------------------

# Returns a sorted list from the tuple

print(sorted(t))

# Output:
# [1, 2, 3, 4]

# ==========================================
# DIFFERENCE BETWEEN LISTS AND TUPLES
# ==========================================

# 1. SYNTAX
# List  -> []
# Tuple -> ()

list1 = [1, 2, 3]
tuple1 = (1, 2, 3)

# ------------------------------------------
# 2. MUTABILITY
# ------------------------------------------

# List  -> Mutable (can be changed)
# Tuple -> Immutable (cannot be changed)

list1[0] = 100      # Valid

# tuple1[0] = 100   # Error

# ------------------------------------------
# 3. SPEED
# ------------------------------------------

# Tuples are generally faster than lists
# because they are immutable.

# List  -> Slower
# Tuple -> Faster

# ------------------------------------------
# 4. MEMORY USAGE
# ------------------------------------------

# Lists consume more memory.
# Tuples consume less memory.

# List  -> More Memory
# Tuple -> Less Memory

# ------------------------------------------
# 5. BUILT-IN FUNCTIONALITY
# ------------------------------------------

# Lists have many built-in methods.
# Tuples have fewer built-in methods.

# List Methods:
# append(), extend(), insert(), remove(),
# pop(), clear(), sort(), reverse()

# Tuple Methods:
# count(), index()

# ------------------------------------------
# 6. ERROR PRONE
# ------------------------------------------

# Lists are more error-prone because data
# can be modified accidentally.

# Tuples are safer because data cannot
# be changed after creation.

# ------------------------------------------
# 7. USABILITY
# ------------------------------------------

# Use Lists:
# When data needs frequent modifications.

# Use Tuples:
# When data should remain fixed and secure.

# Examples:
# List  -> Student names, shopping cart
# Tuple -> Coordinates, days of week

# ==========================================
# TUPLE PACKING
# ==========================================

# Packing means storing multiple values
# into a single tuple.

t = 10, 20, 30, 40

print(t)
print(type(t))

# Output:
# (10, 20, 30, 40)
# <class 'tuple'>

# ==========================================
# TUPLE UNPACKING
# ==========================================

# Unpacking means extracting tuple elements
# into separate variables.

t = (10, 20, 30)

a, b, c = t

print(a)
print(b)
print(c)

# Output:
# 10
# 20
# 30

# ==========================================
# MULTIPLE ASSIGNMENT USING UNPACKING
# ==========================================

name, age, city = ("Nishant", 22, "Nagpur")

print(name)
print(age)
print(city)

# Output:
# Nishant
# 22
# Nagpur

# ==========================================
# VALUE SWAPPING USING TUPLES
# ==========================================

# Swapping values without using a third variable.

a = 10
b = 20

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)

# Output:
# Before Swapping:
# a = 10
# b = 20
#
# After Swapping:
# a = 20
# b = 10

# ==========================================
# EXTENDED TUPLE UNPACKING
# ==========================================

# The * operator is used to collect
# multiple values into a list.

a, b, *others = (1, 2, 3, 4, 5, 6)

print(a)
print(b)
print(others)

# Output:
# 1
# 2
# [3, 4, 5, 6]