# ==========================================
# Program to Replace NaN Values in a NumPy Array
# ==========================================

# Import the NumPy library
import numpy as np

# Create a NumPy array containing numeric values
# and missing values (NaN = Not a Number)
a = np.array([1, 2, np.nan, 4, 5, np.nan])

# Replace all NaN values with 100
c = np.nan_to_num(a, nan=100)

# Display the updated array
print("Array after replacing NaN values:")
print(c)

# Output:
# Array after replacing NaN values:
# [  1.   2. 100.   4.   5. 100.]