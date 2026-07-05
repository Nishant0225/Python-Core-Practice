# ==========================================
# Program to Find the Sum of Squares of the
# First N Natural Numbers
# ==========================================

# Take a number as input from the user
n = int(input("Enter a number: "))

# Initialize the sum variable
sum_of_squares = 0

# Calculate the sum of squares from 1 to n
for i in range(1, n + 1):
    sum_of_squares += i ** 2

# Display the result
print(f"The sum of squares of the first {n} natural numbers is: {sum_of_squares}")

# Example:
# Input: 5
# Calculation: 1² + 2² + 3² + 4² + 5²
#            = 1 + 4 + 9 + 16 + 25
#            = 55
#
# Output:
# The sum of squares of the first 5 natural numbers is: 55