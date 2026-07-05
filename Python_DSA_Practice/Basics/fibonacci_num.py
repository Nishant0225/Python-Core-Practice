# ==========================================
# Program to Check Whether a Number is a
# Fibonacci Number
# ==========================================

# Import the math module for mathematical operations
import math

# Function to check whether a number is a perfect square
def is_perfect_sq(x):
    # Find the square root and convert it to an integer
    s = int(math.sqrt(x))

    # Return True if x is a perfect square, otherwise False
    return s * s == x

# Function to check whether a number is a Fibonacci number
def is_fibonacci(n):
    # A number is a Fibonacci number if either
    # (5 × n² + 4) or (5 × n² - 4) is a perfect square.
    return is_perfect_sq(5 * n * n + 4) or is_perfect_sq(5 * n * n - 4)

# Check numbers from 1 to 6
for i in range(1, 7):

    # Display whether the current number is a Fibonacci number
    if is_fibonacci(i):
        print(f"{i} is a Fibonacci Number.")
    else:
        print(f"{i} is not a Fibonacci Number.")

# Output:
# 1 is a Fibonacci Number.
# 2 is a Fibonacci Number.
# 3 is a Fibonacci Number.
# 4 is not a Fibonacci Number.
# 5 is a Fibonacci Number.
# 6 is not a Fibonacci Number.