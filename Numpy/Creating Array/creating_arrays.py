# ==========================================
# Program to Create Different Types of
# NumPy Arrays
# ==========================================

# Import the NumPy library
import numpy as np

# ------------------------------------------
# Method 1: Create a 1-D Array
# ------------------------------------------

# Create a one-dimensional NumPy array
a = np.array([1, 2, 3, 4, 5, 6])

# ------------------------------------------
# Method 2: Create an Array Filled with a
# Specific Value
# ------------------------------------------

# Create a 2 × 3 array filled with the value 7
b = np.full((2, 3), 7)

# ------------------------------------------
# Method 3: Create an Array of Ones
# ------------------------------------------

# Create a 2 × 3 array filled with 1s
c = np.ones((2, 3))

# ------------------------------------------
# Method 4: Create an Array of Zeros
# ------------------------------------------

# Create a 3 × 3 array filled with 0s
d = np.zeros((3, 3))

# ------------------------------------------
# Display the Arrays
# ------------------------------------------

print("1-D NumPy Array:")
print(a)

print("\n2 × 3 Array Filled with 7:")
print(b)

print("\n2 × 3 Array of Ones:")
print(c)

print("\n3 × 3 Array of Zeros:")
print(d)

# Output:
# 1-D NumPy Array:
# [1 2 3 4 5 6]
#
# 2 × 3 Array Filled with 7:
# [[7 7 7]
#  [7 7 7]]
#
# 2 × 3 Array of Ones:
# [[1. 1. 1.]
#  [1. 1. 1.]]
#
# 3 × 3 Array of Zeros:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]