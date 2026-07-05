# ==========================================
# reduce() FUNCTION IN PYTHON
# ==========================================

# reduce() applies a function cumulatively
# to the elements of an iterable and returns
# a single value.

# reduce() is available in the functools module.

from functools import reduce

# Syntax:
# reduce(function, iterable)

# ------------------------------------------
# SUM OF ALL ELEMENTS
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)

# Output:
# 15

# Calculation:
# (((1+2)+3)+4)+5

# ==========================================
# PRODUCT OF ALL ELEMENTS
# ==========================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers)

print(result)

# Output:
# 120

# Calculation:
# (((1*2)*3)*4)*5

# ==========================================
# FIND MAXIMUM ELEMENT
# ==========================================

from functools import reduce

numbers = [10, 20, 5, 40, 15]

result = reduce(lambda x, y: x if x > y else y, numbers)

print(result)

# Output:
# 40

# ==========================================
# FIND MINIMUM ELEMENT
# ==========================================

from functools import reduce

numbers = [10, 20, 5, 40, 15]

result = reduce(lambda x, y: x if x < y else y, numbers)

print(result)

# Output:
# 5

# ==========================================
# USING NORMAL FUNCTION
# ==========================================

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]

result = reduce(add, numbers)

print(result)

# Output:
# 15

# ==========================================
# map(), filter(), reduce()
# ==========================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() -> Transform
print(list(map(lambda x: x * 2, numbers)))

# filter() -> Select
print(list(filter(lambda x: x % 2 == 0, numbers)))

# reduce() -> Single Result
print(reduce(lambda x, y: x + y, numbers))

# Output:
# [2, 4, 6, 8, 10]
# [2, 4]
# 15

# reduce()

# Purpose:
# Reduces an iterable to a single value.

# Module:
# from functools import reduce

# Syntax:
# reduce(function, iterable)

# Common Uses:
# ✔ Sum of elements
# ✔ Product of elements
# ✔ Maximum value
# ✔ Minimum value

# Returns:
# A single value

# Example:
# reduce(lambda x, y: x + y, [1,2,3,4])
# Output: 10