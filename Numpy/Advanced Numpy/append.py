# ==========================================
# Program to Append Elements to a NumPy Array
# ==========================================

# Import the NumPy library
import numpy as np

# Create a one-dimensional NumPy array
a = np.array([1, 2, 3, 4, 5])

# Append new elements (1 and 2) to the end of the array
new_array = np.append(a, [1, 2])

# Display the updated array
print("Array after appending elements:")
print(new_array)

# Output:
# Array after appending elements:
# [1 2 3 4 5 1 2]