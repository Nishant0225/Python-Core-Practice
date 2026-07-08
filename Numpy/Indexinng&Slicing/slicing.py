# ==========================================
# Program to Access NumPy Array Elements
# Using Slicing
# ==========================================

# Import the NumPy library
import numpy as np

# Create a one-dimensional NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Display elements from index 1 to index 3
# (The ending index is excluded.)
print("Elements from index 1 to 3:")
print(arr[1:4])

# Display elements from the beginning up to index 3
print("\nElements from the beginning to index 3:")
print(arr[:4])

# Output:
# Elements from index 1 to 3:
# [2 3 4]
#
# Elements from the beginning to index 3:
# [1 2 3 4]