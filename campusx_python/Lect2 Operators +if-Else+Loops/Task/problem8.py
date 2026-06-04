# Problem 8:
# Take an integer N as input and find the sum of numbers from 1 to N.
# Skip numbers that are divisible by 5.
# Stop the calculation if the sum becomes greater than 300.
# Print the final sum.
# Do not use a for loop.
#
# Example:
# Input: 30
# Output: 276

a = int(input("Enter a number:"))
sum = 0
i = 1

while i <= a:

    if i % 5 != 0:
        sum = sum + i

    if sum+i > 300:
        break

    i += 1

print(sum)

# Problem solved successfully