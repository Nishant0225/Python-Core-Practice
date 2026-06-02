# Strings in Python

# Strings are a sequence of Unicode characters.

# Topics Covered:
# 1. Creating Strings
s="Hello"
print(s)

# 2. Accessing Strings
#Indexing
s="Hello world"
print(s)

#Positive Indexing
s="Hello world"
print(s[0])

#Negative Indexing
s="Hello world"
print(s[-2])

#Slicing
s="Hello world"
print(s[0:6])

#Slicing Start to end
s="Hello world"
print(s[0::])

#Slicing End to start(Reverse)
s="Hello world"
print(s[::-1])

#Positive Slicing Using Steps
s="Hello world"
print(s[0:6:2])

#Negative Slicing Using Steps
s="Hello world"
print(s[6:0:-2])

# 3. Adding Characters to Strings
# Strings are immutable, so we create a new string instead.

s = "Hello"
s = s + " World"      # Concatenation
print(s)              # Hello World


# 4. Editing Strings
# Strings cannot be changed directly.

s = "Hello"

# s[0] = "Y"    # Error

# Create a new string instead
s = "Y" + s[1:]
print(s)              # Yello


# 5. Deleting Strings

s = "Python"
del s                 # Deletes the entire string variable

# print(s)            # NameError


# 6. Operations on Strings

a = "Hello"
b = "World"

# Arithmetic Operations
print(a + b)          # HelloWorld
print(a * 3)          # HelloHelloHello

# Relational Operations
print("apple" == "apple")   # True
print("apple" < "banana")   # True

# Logical Operations
print("Hello" and "World")  # World
print("" or "Python")       # Python

# Membership Operations
print("H" in a)             # True
print("z" not in a)         # True

# Loops on Strings
for char in a:
    print(char)


# 7. String Functions

s = "python programming"

print(len(s))           # Length of string
print(max(s))           # Highest ASCII/Unicode value
print(min(s))           # Lowest ASCII/Unicode value
print(s.upper())        # PYTHON PROGRAMMING
print(s.lower())        # python programming
print(s.title())        # Python Programming
print(s.capitalize())   # Python programming
print(s.count("m"))     # Count occurrences
print(s.find("gram"))   # Find substring index
print(s.replace("python", "java"))  # Replace text
print(s.split())        # Split into list