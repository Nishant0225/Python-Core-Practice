# ==========================================
# Program to Perform Element-wise Addition
# and Multiplication of NumPy Arrays
# ==========================================

# Import the NumPy library
import numpy as np

# Create the first NumPy array
a = np.array([1, 2, 3, 4])

# Create the second NumPy array
b = np.array([5, 6, 7, 8])

# Perform element-wise addition
addition = a + b

# Perform element-wise multiplication
multiplication = a * b

# Display the result of addition
print("Element-wise Addition:")
print(addition)

# Display the result of multiplication
print("\nElement-wise Multiplication:")
print(multiplication)

# Output:
# Element-wise Addition:
# [ 6  8 10 12]
#
# Element-wise Multiplication:
# [ 5 12 21 32]