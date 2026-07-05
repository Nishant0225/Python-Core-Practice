# ==========================================
# Program to Find the Sum of Cubes of the
# First N Natural Numbers
# ==========================================

# Take a number as input from the user
n = int(input("Enter a number: "))

# Initialize the sum variable
sum_of_cubes = 0

# Calculate the sum of cubes from 1 to n
for i in range(1, n + 1):
    sum_of_cubes += i ** 3

# Display the result
print(f"The sum of cubes of the first {n} natural numbers is: {sum_of_cubes}")

# Example:
# Input: 5
# Calculation: 1³ + 2³ + 3³ + 4³ + 5³
#            = 1 + 8 + 27 + 64 + 125
#            = 225
#
# Output:
# The sum of cubes of the first 5 natural numbers is: 225