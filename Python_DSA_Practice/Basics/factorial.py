# ==========================================
# Program to Find the Factorial of a Number
# ==========================================

# Take a number as input from the user
a = int(input("Enter a number: "))

# Initialize factorial with 1
# (Factorial multiplication always starts from 1)
fact = 1

# Multiply all numbers from 1 to 'a'
for i in range(1, a + 1):
    fact *= i

# Display the factorial
print(f"The factorial of {a} is: {fact}")

# Example:
# Input: 5
# Output: The factorial of 5 is: 120