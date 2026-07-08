# ==========================================
# Program to Access NumPy Array Elements
# Using Boolean Indexing
# ==========================================

# Import the NumPy library
import numpy as np

# Create a one-dimensional NumPy array
a = np.array([1, 2, 3, 4])

# Select and display elements greater than 2
# Boolean indexing returns only the elements
# that satisfy the given condition.
print("Elements greater than 2:")
print(a[a > 2])

# Output:
# Elements greater than 2:
# [3 4]