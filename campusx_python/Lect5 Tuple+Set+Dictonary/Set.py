# ==========================================
# SETS IN PYTHON
# ==========================================

# A set is an unordered collection of unique items.
# Duplicate values are not allowed in a set.

# A set itself is mutable, which means we can
# add or remove elements after creation.

# Sets are commonly used for mathematical
# operations like Union, Intersection,
# Difference, and Symmetric Difference.

# ------------------------------------------
# CHARACTERISTICS OF SETS
# ------------------------------------------

# 1. Unordered
#    - Elements do not maintain insertion order.

# 2. Mutable
#    - Elements can be added or removed.

# 3. No Duplicates
#    - Duplicate values are automatically removed.

# 4. Cannot Contain Mutable Data Types
#    - Lists, dictionaries, and sets cannot be
#      stored inside a set.

# ------------------------------------------
# EXAMPLES
# ------------------------------------------

s1 = {1, 2, 3, 4}
print(s1)

# Duplicate values are removed automatically
s2 = {1, 2, 2, 3, 3, 4}
print(s2)

# Output:
# {1, 2, 3, 4}
# {1, 2, 3, 4}

# ==========================================
# CREATING SETS IN PYTHON
# ==========================================

# ------------------------------------------
# EMPTY SET
# ------------------------------------------

# {} creates an empty dictionary, not a set

s = {}
print(s)
print(type(s))

# Output:
# {}
# <class 'dict'>

# To create an empty set, use set()

s1 = set()
print(s1)
print(type(s1))

# Output:
# set()
# <class 'set'>

# ==========================================
# 1D SET
# ==========================================

s = {1, 2, 3, 4, 5}
print(s)

# Output:
# {1, 2, 3, 4, 5}

# ==========================================
# HOMOGENEOUS SET
# ==========================================

# All elements have the same data type

s = {1, 2, 3, 4, 5}
print(s)

# Output:
# {1, 2, 3, 4, 5}

# ==========================================
# HETEROGENEOUS SET
# ==========================================

# Elements have different data types

s = {1, 2.5, True, "Python"}
print(s)

# Output may vary because sets are unordered

# ==========================================
# USING TYPE CONVERSION
# ==========================================

# Convert a string into a set

s = set("hello")
print(s)

# Output:
# {'h', 'e', 'l', 'o'}

# Duplicate values are removed automatically.

# ==========================================
# DUPLICATES NOT ALLOWED
# ==========================================

s = {1, 2, 2, 3, 3, 4, 4, 5}
print(s)

# Output:
# {1, 2, 3, 4, 5}

# ==========================================
# SET CAN'T HAVE MUTABLE ITEMS
# ==========================================

# Lists are mutable, so they cannot be
# stored inside a set.

# s = {1, 2, [3, 4]}
# print(s)

# Output:
# TypeError: unhashable type: 'list'

# Important Points

# {}          -> Empty Dictionary
# set()       -> Empty Set

# Sets are unordered.
# Sets do not allow duplicates.
# Sets can store immutable data types only.
# Sets automatically remove duplicate values.
# Lists, dictionaries, and sets cannot be
# elements of a set.

# ==========================================
# ACCESSING ITEMS IN A SET
# ==========================================

# Sets do not support indexing or slicing
# because they are unordered collections.

s = {10, 20, 30, 40}

# Invalid Operations

# print(s[0])
# TypeError: 'set' object is not subscriptable

# print(s[1:3])
# TypeError: 'set' object is not subscriptable

# ==========================================
# ACCESSING ITEMS USING LOOP
# ==========================================

s = {10, 20, 30, 40}

for item in s:
    print(item)

# Output may vary because sets are unordered

# ==========================================
# MEMBERSHIP TESTING
# ==========================================

s = {10, 20, 30, 40}

print(20 in s)
print(50 in s)

# Output:
# True
# False

# ==========================================
# CONVERT SET TO LIST/TUPLE
# ==========================================

s = {10, 20, 30, 40}

# Convert to list
l = list(s)
print(l)

# Access elements using indexing
print(l[0])

# Convert to tuple
t = tuple(s)
print(t)

# Accessing Set Elements

# ❌ Indexing not allowed
# ❌ Slicing not allowed

# Reason:
# Sets are unordered collections.

# Ways to access elements:
# 1. Using for loop
# 2. Using membership operators (in, not in)
# 3. Convert set to list or tuple

# ==========================================
# ADDING ITEMS IN A SET
# ==========================================

s = {1, 2, 3}

# add()
# Adds a single element

s.add(4)

print(s)

# Output:
# {1, 2, 3, 4}

# ==========================================
# UPDATING A SET
# ==========================================

s = {1, 2, 3}

# update()
# Adds multiple elements

s.update([4, 5, 6])

print(s)

# Output:
# {1, 2, 3, 4, 5, 6}

# ==========================================
# DIFFERENCE BETWEEN add() AND update()
# ==========================================

s = {1, 2, 3}

s.add(4)              # Single item
s.update([5, 6, 7])   # Multiple items

print(s)

# Output:
# {1, 2, 3, 4, 5, 6, 7}

# ==========================================
# REMOVING ITEMS FROM A SET
# ==========================================

s = {10, 20, 30, 40}

# remove()
# Removes a specific element

s.remove(20)

print(s)

# Output:
# {10, 30, 40}

# ==========================================
# discard()
# ==========================================

s = {10, 20, 30}

s.discard(20)
print(s)

# Output:
# {10, 30}

# If the element is not present,
# discard() does NOT raise an error.

# ==========================================
# pop()
# ==========================================

s = {10, 20, 30, 40}

removed_item = s.pop()

print(removed_item)
print(s)

# Removes and returns a random element
# because sets are unordered.

# ==========================================
# clear()
# ==========================================

s = {1, 2, 3, 4}

s.clear()

print(s)

# Output:
# set()

# ==========================================
# del KEYWORD
# ==========================================

s = {1, 2, 3}

del s

# print(s)
# NameError: name 's' is not defined

# ADD METHODS

# add(x)
# Adds one element.

# update(iterable)
# Adds multiple elements.

# DELETE METHODS

# remove(x)
# Removes element.
# Error if element not found.

# discard(x)
# Removes element.
# No error if element not found.

# pop()
# Removes a random element.

# clear()
# Removes all elements.

# del
# Deletes the entire set.

# ==========================================
# SET OPERATIONS IN PYTHON
# ==========================================

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print("s1 =", s1)
print("s2 =", s2)

# ------------------------------------------
# UNION (|)
# ------------------------------------------
# Combines all unique elements from both sets

print("Union:", s1 | s2)

# Output:
# {1, 2, 3, 4, 5, 6, 7, 8}

# ------------------------------------------
# INTERSECTION (&)
# ------------------------------------------
# Returns common elements

print("Intersection:", s1 & s2)

# Output:
# {4, 5}

# ------------------------------------------
# DIFFERENCE (-)
# ------------------------------------------
# Elements present in first set but not in second

print("s1 - s2:", s1 - s2)
print("s2 - s1:", s2 - s1)

# Output:
# {1, 2, 3}
# {6, 7, 8}

# ------------------------------------------
# SYMMETRIC DIFFERENCE (^)
# ------------------------------------------
# Elements present in either set
# but not in both

print("Symmetric Difference:", s1 ^ s2)

# Output:
# {1, 2, 3, 6, 7, 8}

# ------------------------------------------
# MEMBERSHIP TEST
# ------------------------------------------

print(3 in s1)
print(10 in s1)

# Output:
# True
# False

# ------------------------------------------
# ITERATION
# ------------------------------------------

for item in s1:
    print(item)

# Output may vary because sets are unordered

# Set Operations

# |  -> Union
# &  -> Intersection
# -  -> Difference
# ^  -> Symmetric Difference
# in -> Membership Test
# for loop -> Iteration

# Example:
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}

# s1 | s2 -> {1, 2, 3, 4, 5, 6, 7, 8}
# s1 & s2 -> {4, 5}
# s1 - s2 -> {1, 2, 3}
# s1 ^ s2 -> {1, 2, 3, 6, 7, 8}

# ==========================================
# COMMON FUNCTIONS USED WITH SETS
# ==========================================

s = {3, 1, 4, 5, 2, 7}

# ------------------------------------------
# len()
# ------------------------------------------

# Returns the number of elements

print(len(s))

# Output:
# 6

# ------------------------------------------
# sum()
# ------------------------------------------

# Returns the sum of all elements

print(sum(s))

# Output:
# 22

# ------------------------------------------
# min()
# ------------------------------------------

# Returns the smallest element

print(min(s))

# Output:
# 1

# ------------------------------------------
# max()
# ------------------------------------------

# Returns the largest element

print(max(s))

# Output:
# 7

# ------------------------------------------
# sorted()
# ------------------------------------------

# Returns a sorted list

print(sorted(s))

# Output:
# [1, 2, 3, 4, 5, 7]

# ------------------------------------------
# union() / update()
# ------------------------------------------

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.union(s2))

s1.update(s2)
print(s1)

# Output:
# {1, 2, 3, 4, 5, 6, 7, 8}
# {1, 2, 3, 4, 5, 6, 7, 8}

# ------------------------------------------
# intersection() / intersection_update()
# ------------------------------------------

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.intersection(s2))

s1.intersection_update(s2)
print(s1)

# Output:
# {4, 5}
# {4, 5}

# ------------------------------------------
# difference() / difference_update()
# ------------------------------------------

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.difference(s2))

s1.difference_update(s2)
print(s1)

# Output:
# {1, 2, 3}
# {1, 2, 3}

# ------------------------------------------
# symmetric_difference()
# ------------------------------------------

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.symmetric_difference(s2))

# Output:
# {1, 2, 3, 6, 7, 8}

# Set Functions

# len(s)                     -> Number of elements
# sum(s)                     -> Sum of elements
# min(s)                     -> Smallest element
# max(s)                     -> Largest element
# sorted(s)                  -> Sorted list

# union()                    -> Combines sets
# update()                   -> Adds all elements to original set

# intersection()             -> Common elements
# intersection_update()      -> Updates original set

# difference()               -> Unique elements
# difference_update()        -> Updates original set

# symmetric_difference()     -> Non-common elements

# ==========================================
# isdisjoint(), issubset(), issuperset()
# ==========================================

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# ------------------------------------------
# isdisjoint()
# ------------------------------------------

# Returns True if both sets have
# no common elements.

print(s1.isdisjoint(s2))

# Output:
# False

# Because 3 and 4 are common.

# Example of isdisjoint()

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))

# Output:
# True

# ------------------------------------------
# issubset()
# ------------------------------------------

# Returns True if all elements of one set
# are present in another set.

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))

# Output:
# True

# ------------------------------------------
# issuperset()
# ------------------------------------------

# Returns True if a set contains all
# elements of another set.

a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))

# Output:
# True

# ==========================================
# COMBINED EXAMPLE
# ==========================================

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {1, 2}

print(s1.isdisjoint(s2))  # False
print(s3.issubset(s1))    # True
print(s1.issuperset(s3))  # True

# isdisjoint()
# Checks whether two sets have
# no common elements.

# issubset()
# Checks whether all elements of one set
# exist in another set.

# issuperset()
# Checks whether a set contains all
# elements of another set.

# Memory Trick

# subset   -> Small set inside big set
# superset -> Big set contains small set
# disjoint -> No common elements

# ==========================================
# FROZENSET IN PYTHON
# ==========================================

# A frozenset is an immutable version of a set.
# Once created, elements cannot be modified,
# added, or removed.

# Syntax:
# frozenset(iterable)

# ------------------------------------------
# CREATING A FROZENSET
# ------------------------------------------

fs = frozenset([1, 2, 3])

print(fs)

# Output:
# frozenset({1, 2, 3})

# ------------------------------------------
# READ OPERATIONS (WORKS)
# ------------------------------------------

print(len(fs))      # Number of elements
print(min(fs))      # Smallest element
print(max(fs))      # Largest element
print(sum(fs))      # Sum of elements

print(2 in fs)      # Membership Test

# Output:
# 3
# 1
# 3
# 6
# True

# ------------------------------------------
# WRITE OPERATIONS (DOES NOT WORK)
# ------------------------------------------

# fs.add(4)
# fs.remove(2)
# fs.update([4, 5])

# Output:
# AttributeError

# ------------------------------------------
# SET OPERATIONS
# ------------------------------------------

fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])

print("Union:", fs1 | fs2)
print("Intersection:", fs1 & fs2)
print("Difference:", fs1 - fs2)
print("Symmetric Difference:", fs1 ^ fs2)

# Output:
# Union: frozenset({1, 2, 3, 4, 5, 6})
# Intersection: frozenset({3, 4})
# Difference: frozenset({1, 2})
# Symmetric Difference: frozenset({1, 2, 5, 6})

# ------------------------------------------
# USING FROZENSET INSIDE A SET
# ------------------------------------------

fs = frozenset([1, 2, 3])

s = {fs}

print(s)

# Output:
# {frozenset({1, 2, 3})}

# ------------------------------------------
# 2D SETS USING FROZENSET
# ------------------------------------------

s = {
    frozenset({1, 2}),
    frozenset({3, 4})
}

print(s)

# Output:
# {frozenset({1, 2}), frozenset({3, 4})}