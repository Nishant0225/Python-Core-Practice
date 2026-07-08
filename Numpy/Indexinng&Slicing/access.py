# ==========================================
# Program to Access Elements of a NumPy Array
# Using Indexing
# ==========================================

# Import the NumPy library
import numpy as np

# Create a one-dimensional NumPy array
a = np.array([1, 2, 3, 4])

# Access the first element (index 0)
print(f"The element at index 0 is: {a[0]}")

# Access the third element (index 2)
print(f"The element at index 2 is: {a[2]}")

# Access the last element using negative indexing
print(f"The last element of the array is: {a[-1]}")

# Output:
# The element at index 0 is: 1
# The element at index 2 is: 3
# The last element of the array is: 4