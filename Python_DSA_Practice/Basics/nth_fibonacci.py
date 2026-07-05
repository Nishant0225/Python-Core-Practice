# ==========================================
# Program to Find the Nth Fibonacci Number
# Using Recursion
# ==========================================

# Take the position (n) as input from the user
n = int(input("Enter the position of the Fibonacci number: "))

# Function to calculate the nth Fibonacci number recursively
def fibonacci(n):
    # Base Case:
    # If n is 0 or 1, return n
    if n <= 1:
        return n

    # Recursive Case:
    # Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

# Display the nth Fibonacci number
print(f"The Fibonacci number at position {n} is: {fibonacci(n)}")

# Example:
# Input: 9
# Output: The Fibonacci number at position 9 is: 34