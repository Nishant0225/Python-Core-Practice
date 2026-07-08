# ==========================================
# Program to Delete Elements from NumPy Arrays
# ==========================================

# Import the NumPy library
import numpy as np

# ------------------------------------------
# Delete an Element from a 1-D Array
# ------------------------------------------

# Create a one-dimensional NumPy array
a = np.array([1, 2, 3, 4, 5])

# Delete the element at index 1
b = np.delete(a, 1)

# Display the updated array
print("1-D Array after deleting the element at index 1:")
print(b)

# ------------------------------------------
# Delete a Row from a 2-D Array
# ------------------------------------------

# Create a two-dimensional NumPy array
c = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

# Delete the first row (index 0)
d = np.delete(c, 0, axis=0)

# Display the updated array
print("\n2-D Array after deleting the first row:")
print(d)

# Output:
# 1-D Array after deleting the element at index 1:
# [1 3 4 5]
#
# 2-D Array after deleting the first row:
# [[ 6  7  8  9 10]]