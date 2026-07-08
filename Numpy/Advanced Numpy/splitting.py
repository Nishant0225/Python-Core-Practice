# ==========================================
# Program to Split a NumPy Array
# ==========================================

# Import the NumPy library
import numpy as np

# Create a one-dimensional NumPy array
a = np.array([1, 2, 3, 4, 5, 6])

# Split the array into 2 equal parts
split_array = np.split(a, 2)

# Display the split arrays
print("Array after splitting into 2 equal parts:")
print(split_array)

# Output:
# Array after splitting into 2 equal parts:
# [array([1, 2, 3]), array([4, 5, 6])]