# ==========================================
# Program to Find the Remainder When the
# Product of All List Elements is Divided
# by a Given Number
# ==========================================

# Create a list of numbers
l = [1, 2, 3, 4, 5, 6]

# Take the divisor as input from the user
n = int(input("Enter a number: "))

# Initialize the product variable
product = 1

# Multiply all elements of the list
for num in l:
    product *= num

# Find the remainder when the product is divided by n
remainder = product % n

# Display the result
print(f"The remainder when the product of all list elements is divided by {n} is: {remainder}")

# Example:
# List: [1, 2, 3, 4, 5, 6]
# Product = 1 × 2 × 3 × 4 × 5 × 6 = 720
#
# Input:
# n = 7
#
# Output:
# The remainder when the product of all list elements is divided by 7 is: 6