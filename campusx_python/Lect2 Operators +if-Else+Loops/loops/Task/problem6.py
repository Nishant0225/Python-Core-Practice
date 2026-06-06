# Problem 6 - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
# For example: calculate the factorial of 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Output:
# 120

# Take a number as input from the user
n = int(input("Enter a number: "))

# Initialize factorial value to 1
temp = 1

# Multiply all numbers from 1 to n
for i in range(1, n + 1):
    temp = temp * i

# Display the factorial
print("Factorial =", temp)