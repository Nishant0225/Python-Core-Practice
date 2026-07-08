# ==========================================
# Program to Concatenate Two NumPy Arrays
# ==========================================

# Import the NumPy library
import numpy as np

# Create the first one-dimensional NumPy array
a = np.array([1, 2, 3, 4, 5])

# Create the second one-dimensional NumPy array
b = np.array([6, 7, 8, 9])

# Concatenate the two arrays
new_array = np.concatenate((a, b))

# Display the concatenated array
print("Array after concatenation:")
print(new_array)

# Output:
# Array after concatenation:
# [1 2 3 4 5 6 7 8 9]