# ==========================================
# Program to Create an Identity Matrix
# Using NumPy
# ==========================================

# Import the NumPy library
import numpy as np

# Create a 3 × 3 identity matrix
# An identity matrix has 1s on the main diagonal
# and 0s in all other positions.
a = np.eye(3)

# Display the identity matrix
print("3 × 3 Identity Matrix:")
print(a)

# Output:
# 3 × 3 Identity Matrix:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]