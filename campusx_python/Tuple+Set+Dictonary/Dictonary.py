# ==========================================
# DICTIONARY IN PYTHON
# ==========================================

# A dictionary is a collection of key-value pairs.
# It is used to store data in the form of
# key : value.

# Dictionaries are also known as:
# - Map
# - Associative Array

# Example:

student = {
    "name": "Nitish",
    "age": 33,
    "gender": "Male"
}

print(student)

# Output:
# {'name': 'Nitish', 'age': 33, 'gender': 'Male'}

# ------------------------------------------
# CHARACTERISTICS OF DICTIONARY
# ------------------------------------------

# 1. Mutable
#    - Values can be added, updated, or removed.

# 2. Indexing Has No Meaning
#    - Elements are accessed using keys,
#      not indexes.

# 3. Keys Must Be Unique
#    - Duplicate keys are not allowed.

# 4. Keys Must Be Immutable
#    - Keys can be string, number, tuple, etc.
#    - Lists, sets, and dictionaries cannot
#      be used as keys.

# ------------------------------------------
# EXAMPLES
# ------------------------------------------

# Mutable

student["age"] = 34
print(student)

# Unique Keys

d = {
    "name": "Nishant",
    "name": "Rahul"
}

print(d)

# Output:
# {'name': 'Rahul'}
# Last value overwrites previous value.

# Immutable Keys

d = {
    1: "One",
    (1, 2): "Tuple Key"
}

print(d)

# Valid Keys

# Invalid Example

# d = {
#     [1, 2]: "List Key"
# }

# Output:
# TypeError: unhashable type: 'list'

# ==========================================
# CREATING DICTIONARIES IN PYTHON
# ==========================================

# ------------------------------------------
# EMPTY DICTIONARY
# ------------------------------------------

d1 = {}

print(d1)
print(type(d1))

# Output:
# {}
# <class 'dict'>

# ------------------------------------------
# 1D DICTIONARY
# ------------------------------------------

student = {
    "name": "Nishant",
    "age": 22,
    "city": "Nagpur"
}

print(student)

# Output:
# {'name': 'Nishant', 'age': 22, 'city': 'Nagpur'}

# ------------------------------------------
# DICTIONARY WITH MIXED KEYS
# ------------------------------------------

d2 = {
    "name": "Nishant",
    1: "One",
    (10, 20): "Tuple Key"
}

print(d2)

# Output:
# {'name': 'Nishant', 1: 'One', (10, 20): 'Tuple Key'}

# ------------------------------------------
# 2D (NESTED) DICTIONARY
# ------------------------------------------

students = {
    101: {
        "name": "Nishant",
        "age": 22
    },
    102: {
        "name": "Rahul",
        "age": 21
    }
}

print(students)

# Output:
# {101: {'name': 'Nishant', 'age': 22},
#  102: {'name': 'Rahul', 'age': 21}}

# ------------------------------------------
# USING dict() FUNCTION
# ------------------------------------------

d3 = dict(name="Nishant", age=22, city="Nagpur")

print(d3)

# Output:
# {'name': 'Nishant', 'age': 22, 'city': 'Nagpur'}

# ------------------------------------------
# USING SEQUENCE
# ------------------------------------------

d4 = dict([
    ("name", "Nishant"),
    ("age", 22),
    ("city", "Nagpur")
])

print(d4)

# Output:
# {'name': 'Nishant', 'age': 22, 'city': 'Nagpur'}

# ------------------------------------------
# DUPLICATE KEYS
# ------------------------------------------

d5 = {
    "name": "Nishant",
    "name": "Rahul"
}

print(d5)

# Output:
# {'name': 'Rahul'}

# Last value overwrites previous value.

# ------------------------------------------
# MUTABLE ITEMS AS KEYS
# ------------------------------------------

# Lists cannot be used as keys because
# they are mutable.

# d6 = {
#     [1, 2]: "Python"
# }

# Output:
# TypeError: unhashable type: 'list'

# ==========================================
# ACCESSING ITEMS IN A DICTIONARY
# ==========================================

student = {
    "name": "Nishant",
    "age": 22,
    "city": "Nagpur"
}

# Dictionaries are accessed using KEYS,
# not indexes.

# ------------------------------------------
# ACCESS USING KEY
# ------------------------------------------

print(student["name"])
print(student["age"])

# Output:
# Nishant
# 22

# ------------------------------------------
# ACCESS USING get()
# ------------------------------------------

print(student.get("city"))

# Output:
# Nagpur

# get() returns None if key is not found.
print(student.get("gender"))

# Output:
# None

# ------------------------------------------
# ACCESS ALL KEYS
# ------------------------------------------

print(student.keys())

# Output:
# dict_keys(['name', 'age', 'city'])

# ------------------------------------------
# ACCESS ALL VALUES
# ------------------------------------------

print(student.values())

# Output:
# dict_values(['Nishant', 22, 'Nagpur'])

# ------------------------------------------
# ACCESS ALL KEY-VALUE PAIRS
# ------------------------------------------

print(student.items())

# Output:
# dict_items([('name', 'Nishant'),
#             ('age', 22),
#             ('city', 'Nagpur')])

# ==========================================
# ADDING & UPDATING KEY-VALUE PAIRS
# ==========================================

student = {
    "name": "Nishant",
    "age": 22
}

print("Original Dictionary:")
print(student)

# ------------------------------------------
# ADD A NEW KEY-VALUE PAIR
# ------------------------------------------

student["city"] = "Nagpur"

print("\nAfter Adding city:")
print(student)

# Output:
# {'name': 'Nishant', 'age': 22, 'city': 'Nagpur'}

# ------------------------------------------
# UPDATE AN EXISTING VALUE
# ------------------------------------------

student["age"] = 23

print("\nAfter Updating age:")
print(student)

# Output:
# {'name': 'Nishant', 'age': 23, 'city': 'Nagpur'}

# ------------------------------------------
# USING update()
# ------------------------------------------

student.update({
    "gender": "Male",
    "country": "India"
})

print("\nAfter update():")
print(student)

# Output:
# {'name': 'Nishant',
#  'age': 23,
#  'city': 'Nagpur',
#  'gender': 'Male',
#  'country': 'India'}

# ------------------------------------------
# ADD MULTIPLE KEY-VALUE PAIRS
# ------------------------------------------

student.update(
    college="HVPM",
    branch="IT"
)

print("\nAfter Adding Multiple Keys:")
print(student)

# Output:
# {'name': 'Nishant', 'age': 23, 'city': 'Nagpur',
#  'gender': 'Male', 'country': 'India',
#  'college': 'HVPM', 'branch': 'IT'}

# ==========================================
# REMOVING KEY-VALUE PAIRS FROM DICTIONARY
# ==========================================

student = {
    "name": "Nishant",
    "age": 22,
    "city": "Nagpur",
    "gender": "Male"
}

print("Original Dictionary:")
print(student)

# ------------------------------------------
# pop()
# ------------------------------------------

# Removes the specified key
# and returns its value.

removed_value = student.pop("city")

print("\nRemoved Value:", removed_value)
print(student)

# Output:
# Removed Value: Nagpur
# {'name': 'Nishant', 'age': 22, 'gender': 'Male'}

# ------------------------------------------
# popitem()
# ------------------------------------------

# Removes the last inserted key-value pair.

item = student.popitem()

print("\nRemoved Item:", item)
print(student)

# Output:
# ('gender', 'Male')
# {'name': 'Nishant', 'age': 22}

# ------------------------------------------
# del
# ------------------------------------------

# Deletes a specific key-value pair.

del student["age"]

print("\nAfter del:")
print(student)

# Output:
# {'name': 'Nishant'}

# ------------------------------------------
# clear()
# ------------------------------------------

# Removes all key-value pairs.

student.clear()

print("\nAfter clear():")
print(student)

# Output:
# {}