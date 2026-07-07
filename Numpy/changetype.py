# ==========================================
# Program to Change the Data Type (dtype)
# of a NumPy Array
# ==========================================

# Import the NumPy library
import numpy as np

# Create a NumPy array of integers
a = np.array([1, 2, 3, 4, 5])

# Display the original data type
print(f"Original data type: {a.dtype}")

# Convert the array from integer to float
b = a.astype(float)

# Display the new array
print("Array after changing the data type:")
print(b)

# Display the new data type
print(f"New data type: {b.dtype}")

# Output:
# Original data type: int64
# Array after changing the data type:
# [1. 2. 3. 4. 5.]
# New data type: float64