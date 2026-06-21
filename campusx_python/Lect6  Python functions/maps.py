# ==========================================
# map() FUNCTION IN PYTHON
# ==========================================

# map() applies a function to every element
# of an iterable and returns a map object.

# Syntax:
# map(function, iterable)

# ------------------------------------------
# USING NORMAL FUNCTION
# ------------------------------------------

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

result = map(square, numbers)

print(list(result))

# Output:
# [1, 4, 9, 16, 25]

# ------------------------------------------
# USING LAMBDA FUNCTION
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * x, numbers)

print(list(result))

# Output:
# [1, 4, 9, 16, 25]

# ------------------------------------------
# MULTIPLY EACH ELEMENT BY 2
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))

# Output:
# [2, 4, 6, 8, 10]

# ------------------------------------------
# USING map() WITH MULTIPLE ITERABLES
# ------------------------------------------

l1 = [1, 2, 3]
l2 = [4, 5, 6]

result = map(lambda x, y: x + y, l1, l2)

print(list(result))

# Output:
# [5, 7, 9]

# ------------------------------------------
# CONVERT STRINGS TO UPPERCASE
# ------------------------------------------

names = ["rahul", "aman", "nishant"]

result = map(str.upper, names)

print(list(result))

# Output:
# ['RAHUL', 'AMAN', 'NISHANT']

# ==========================================
# NOTES
# ==========================================

# map()
# - Applies a function to every element.
# - Returns a map object.
# - Use list() to view the result.
# - Commonly used with lambda functions.

# Syntax:
# map(function, iterable)

# Example:
# list(map(lambda x: x*2, [1,2,3]))
# Output: [2,4,6]

# ==========================================
# DIFFERENCE: LOOP vs map()
# ==========================================

numbers = [1, 2, 3, 4, 5]

# Using Loop
result = []

for i in numbers:
    result.append(i * 2)

print(result)

# Using map()
result = list(map(lambda x: x * 2, numbers))

print(result)

# Output:
# [2, 4, 6, 8, 10]
# [2, 4, 6, 8, 10]