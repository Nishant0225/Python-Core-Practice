# ==========================================
# Program to Reshape a NumPy Array
# ==========================================

# Import the NumPy library
import numpy as np

# Create a one-dimensional NumPy array
a = np.array([1, 2, 3, 4, 5, 6])

# Reshape the 1-D array into a 2 × 3 array
reshape_arr = a.reshape(2, 3)

# Display the reshaped array
print("Reshaped Array (2 × 3):")
print(reshape_arr)

# Output:
# Reshaped Array (2 × 3):
# [[1 2 3]
#  [4 5 6]]