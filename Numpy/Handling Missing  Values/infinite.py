# ==========================================
# Program to Replace Positive and Negative
# Infinity Values in a NumPy Array
# ==========================================

# Import the NumPy library
import numpy as np

# Create a NumPy array containing
# positive and negative infinity values
a = np.array([1, 2, np.inf, 4, 5, -np.inf])

# Replace:
# +Infinity with 100
# -Infinity with -100
b = np.nan_to_num(a, posinf=100, neginf=-100)

# Display the updated array
print("Array after replacing infinity values:")
print(b)

# Output:
# Array after replacing infinity values:
# [   1.    2.  100.    4.    5. -100.]