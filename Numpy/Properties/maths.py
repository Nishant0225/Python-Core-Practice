# ==========================================
# NumPy Arithmetic Operations
# ==========================================

# Import the NumPy library
import numpy as np

# Create two NumPy arrays
a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

# ------------------------------------------
# Addition
# ------------------------------------------
print("Addition of two arrays:")
print(a + b)

# ------------------------------------------
# Subtraction
# ------------------------------------------
print("\nSubtraction of two arrays:")
print(a - b)

# ------------------------------------------
# Multiplication
# ------------------------------------------
print("\nMultiplication of two arrays:")
print(a * b)

# ------------------------------------------
# Division
# ------------------------------------------
print("\nDivision of two arrays:")
print(a / b)

# ------------------------------------------
# Floor Division
# ------------------------------------------
print("\nFloor Division of two arrays:")
print(a // b)

# ------------------------------------------
# Modulus (Remainder)
# ------------------------------------------
print("\nModulus of two arrays:")
print(a % b)

# ------------------------------------------
# Exponentiation (Power)
# ------------------------------------------
print("\nExponentiation of two arrays:")
print(a ** b)

# Output:
# Addition:
# [12 24 35 48]
#
# Subtraction:
# [ 8 16 25 32]
#
# Multiplication:
# [ 20  80 150 320]
#
# Division:
# [5. 5. 6. 5.]
#
# Floor Division:
# [5 5 6 5]
#
# Modulus:
# [0 0 0 0]
#
# Exponentiation:
# [      100 160000 24300000 6553600000000]