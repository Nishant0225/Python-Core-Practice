# ==========================================
# Program to Flatten a NumPy Array
# Using ravel() and flatten()
# ==========================================

# Import the NumPy library
import numpy as np

# Create a 2-dimensional NumPy array
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

# Convert the 2-D array into a 1-D array using ravel()
print("Array after using ravel():")
print(a.ravel())

# Convert the 2-D array into a 1-D array using flatten()
print("\nArray after using flatten():")
print(a.flatten())

# Output:
# Array after using ravel():
# [1 2 3 4 5 6 7 8]
#
# Array after using flatten():
# [1 2 3 4 5 6 7 8]