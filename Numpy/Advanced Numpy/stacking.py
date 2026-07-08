# ==========================================
# Program to Stack NumPy Arrays Vertically
# and Horizontally
# ==========================================

# Import the NumPy library
import numpy as np

# Create two one-dimensional NumPy arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

# ------------------------------------------
# Vertical Stacking (vstack)
# ------------------------------------------

# Stack the arrays vertically (row-wise)
print("Arrays after Vertical Stacking (vstack):")
print(np.vstack((a, b)))

# ------------------------------------------
# Horizontal Stacking (hstack)
# ------------------------------------------

# Stack the arrays horizontally (column-wise)
print("\nArrays after Horizontal Stacking (hstack):")
print(np.hstack((a, b)))

# Output:
# Arrays after Vertical Stacking (vstack):
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
#
# Arrays after Horizontal Stacking (hstack):
# [ 1  2  3  4  5  6  7  8  9 10]