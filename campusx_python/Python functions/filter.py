# ==========================================
# filter() FUNCTION IN PYTHON
# ==========================================

# filter() is used to filter elements
# from an iterable based on a condition.

# Syntax:
# filter(function, iterable)

# It returns a filter object.

# ------------------------------------------
# USING NORMAL FUNCTION
# ------------------------------------------

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

result = filter(is_even, numbers)

print(list(result))

# Output:
# [2, 4, 6]

# ------------------------------------------
# USING LAMBDA FUNCTION
# ------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

# Output:
# [2, 4, 6]

# ------------------------------------------
# FILTER ODD NUMBERS
# ------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 != 0, numbers)

print(list(result))

# Output:
# [1, 3, 5]

# ------------------------------------------
# FILTER NUMBERS GREATER THAN 5
# ------------------------------------------

numbers = [2, 4, 6, 8, 10]

result = filter(lambda x: x > 5, numbers)

print(list(result))

# Output:
# [6, 8, 10]

# ------------------------------------------
# FILTER STRINGS
# ------------------------------------------

names = ["Rahul", "", "Aman", "", "Nishant"]

result = filter(None, names)

print(list(result))

# Output:
# ['Rahul', 'Aman', 'Nishant']

# ==========================================
# NOTES
# ==========================================

# filter()
# - Filters elements based on a condition.
# - Returns a filter object.
# - Use list() to view the result.

# Syntax:
# filter(function, iterable)

# Example:
# list(filter(lambda x: x % 2 == 0, [1,2,3,4]))

# Output:
# [2, 4]

# ==========================================
# DIFFERENCE: map() vs filter()
# ==========================================

numbers = [1, 2, 3, 4, 5]

# map() -> Transforms elements
print(list(map(lambda x: x * 2, numbers)))

# filter() -> Selects elements
print(list(filter(lambda x: x % 2 == 0, numbers)))

# Output:
# [2, 4, 6, 8, 10]
# [2, 4]