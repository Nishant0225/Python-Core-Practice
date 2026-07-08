# ==========================================
# Program to Demonstrate NumPy Broadcasting
# ==========================================

# Import the NumPy library
import numpy as np

# Create a 2-dimensional NumPy array (Matrix)
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

# Create a one-dimensional NumPy array
a = np.array([10, 20, 30, 40, 50])

# Multiply the matrix with the 1-D array
# NumPy automatically broadcasts the 1-D array
# to match the shape of the matrix.
result = matrix * a

# Display the resulting array
print("Result after broadcasting multiplication:")
print(result)

# Output:
# Result after broadcasting multiplication:
# [[ 10  40  90 160 250]
#  [ 60 140 240 360 500]]