# ==========================================
# LAMBDA FUNCTION IN PYTHON
# ==========================================

# A lambda function is a small anonymous
# (nameless) function.

# It is used for short, one-line functions.

# Syntax:
# lambda arguments : expression

# Example

square = lambda x: x * x

print(square(5))

# Output:
# 25

# ==========================================
# NORMAL FUNCTION VS LAMBDA FUNCTION
# ==========================================

# Normal Function

def square(x):
    return x * x

print(square(5))

# Lambda Function

square = lambda x: x * x

print(square(5))

# Output:
# 25
# 25

# ==========================================
# LAMBDA WITH MULTIPLE ARGUMENTS
# ==========================================

add = lambda a, b: a + b

print(add(10, 20))

# Output:
# 30

# ==========================================
# LAMBDA WITH CONDITIONAL EXPRESSION
# ==========================================

is_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(is_even(10))
print(is_even(7))

# Output:
# Even
# Odd

# ==========================================
# LAMBDA WITH sorted()
# ==========================================

students = [
    ("Rahul", 85),
    ("Nishant", 95),
    ("Aman", 75)
]

result = sorted(students, key=lambda x: x[1])

print(result)

# Output:
# [('Aman', 75),
#  ('Rahul', 85),
#  ('Nishant', 95)]

# ==========================================
# LAMBDA WITH map()
# ==========================================

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

# Output:
# [2, 4, 6, 8, 10]

# ==========================================
# LAMBDA WITH filter()
# ==========================================

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

# Output:
# [2, 4, 6]

# Lambda Function

# A lambda function is an anonymous
# one-line function.

# Syntax:
# lambda arguments : expression

# Features:
# ✔ No function name
# ✔ Single expression only
# ✔ Returns value automatically
# ✔ Useful for short operations

# Commonly Used With:
# map()
# filter()
# sorted()