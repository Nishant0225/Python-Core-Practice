# ==========================================
# Program to Create a NumPy Array
# Containing Missing Values (NaN)
# ==========================================

# Import the NumPy library
import numpy as np

# Create a NumPy array containing numeric values
# and missing values (NaN = Not a Number)
a = np.array([1, 2, np.nan, 4, 5, np.nan])

# Display the array
print("NumPy array with missing values:")
print(a)

# Output:
# NumPy array with missing values:
# [ 1.  2. nan  4.  5. nan]