# Problem 6: Find the factorial of a given number.
#
# Write a program that uses a loop to find the factorial of a given number.
#
# The factorial (symbol: !) of a number is the product of all
# positive integers from that number down to 1.
#
# Example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
#
# Input:
# 5
#
# Output:
# 120

# Take a number as input from the user
a = int(input("Enter number for finding factorial: "))

# Initialize a variable to store the factorial result
temp = 1

# Multiply all numbers from 1 to the given number
for i in range(1, a + 1):
    temp = temp * i

# Display the factorial of the given number
print(temp)

# Problem solved successfully