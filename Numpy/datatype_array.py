# ==========================================
# Program to Find the Data Type (dtype)
# of a NumPy Array
# ==========================================

# Import the NumPy library
import numpy as np

# Create a NumPy array
a = np.array([
    [1, 2, 3],
    [8, 9, 10]
])

# Display the data type of the array elements
# dtype represents the type of data stored in the array
print(f"The data type of the array is: {a.dtype}")

# Output:
# The data type of the array is: int64
# (On some systems, it may display int32.)