# ==========================================
# Collection of Objects in Python
# ==========================================

# Definition:
# A Collection of Objects means storing multiple objects
# together in a single data structure like a List, Tuple,
# Set, or Dictionary.

# Why use Collection of Objects?
# • To store multiple objects together.
# • Easy to access and manage objects.
# • Can perform operations on all objects using loops.
# • Makes the program organized and efficient.

# Types of Collection:
# 1. List of Objects
# 2. Tuple of Objects
# 3. Set of Objects
# 4. Dictionary of Objects


# ==========================================
# Creating a Class
# ==========================================

class Person:

    # Constructor
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# ==========================================
# Creating Objects
# ==========================================

p1 = Person("Nitish", "Male")
p2 = Person("Ankit", "Male")
p3 = Person("Tanvi", "Female")


# ==========================================
# 1. List of Objects
# ==========================================

print("----- List of Objects -----")

people_list = [p1, p2, p3]

for person in people_list:
    print(person.name, "-", person.gender)


# ==========================================
# 2. Tuple of Objects
# ==========================================

print("\n----- Tuple of Objects -----")

people_tuple = (p1, p2, p3)

for person in people_tuple:
    print(person.name, "-", person.gender)


# ==========================================
# 3. Set of Objects
# ==========================================

print("\n----- Set of Objects -----")

people_set = {p1, p2, p3}

for person in people_set:
    print(person.name, "-", person.gender)


# ==========================================
# 4. Dictionary of Objects
# ==========================================

print("\n----- Dictionary of Objects -----")

people_dict = {
    101: p1,
    102: p2,
    103: p3
}

for roll_no, person in people_dict.items():
    print(roll_no, ":", person.name, "-", person.gender)


# ==========================================
# Output
# ==========================================

# ----- List of Objects -----
# Nitish - Male
# Ankit - Male
# Tanvi - Female
#
# ----- Tuple of Objects -----
# Nitish - Male
# Ankit - Male
# Tanvi - Female
#
# ----- Set of Objects -----
# (Order may vary because Set is unordered)
#
# ----- Dictionary of Objects -----
# 101 : Nitish - Male
# 102 : Ankit - Male
# 103 : Tanvi - Female


# ==========================================
# Short Notes
# ==========================================

# Collection of Objects:
# A collection of objects means storing multiple objects
# in one data structure such as a List, Tuple, Set,
# or Dictionary.

# Advantages:
# • Stores multiple objects together.
# • Easy to access using loops.
# • Better data organization.
# • Reduces code repetition.
# • Makes object management simple.

# Interview Definition:
# Collection of Objects is the process of storing multiple
# objects of the same or different classes in a single
# collection (List, Tuple, Set, Dictionary) so they can
# be accessed, managed, and processed efficiently.