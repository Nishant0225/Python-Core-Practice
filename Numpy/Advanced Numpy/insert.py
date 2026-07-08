# ==========================================
# Program to Insert Elements into a NumPy Array
# ==========================================

# Import the NumPy library
import numpy as np

# ------------------------------------------
# Method 1: Insert an Element into a
# One-Dimensional Array
# ------------------------------------------

# Create a one-dimensional NumPy array
a = np.array([1, 2, 3, 4, 5, 6])

# Insert the value 4 at index 2
b = np.insert(a, 2, 4)

# Display the updated array
print("1-D Array after insertion:")
print(b)

# ------------------------------------------
# Method 2: Insert a Row into a
# Two-Dimensional Array
# ------------------------------------------

# Create a two-dimensional NumPy array
a1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Insert a new row at index 1
b1 = np.insert(a1, 1, [2, 3, 5], axis=0)

# Display the updated 2-D array
print("\n2-D Array after inserting a row:")
print(b1)

# Output:
# 1-D Array after insertion:
# [1 2 4 3 4 5 6]
#
# 2-D Array after inserting a row:
# [[1 2 3]
#  [2 3 5]
#  [4 5 6]]