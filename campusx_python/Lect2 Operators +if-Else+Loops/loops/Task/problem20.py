# Program to find the sum of the series:
# 1 + x^2/2 + x^3/3 + ... + x^n/n

# Input the value of n (number of terms)
n = int(input("Enter value of n: "))

# Input the value of x
x = int(input("Enter value of x: "))

# Initialize the sum with the first term of the series
sum = 1

# Calculate and add the remaining terms of the series
for i in range(2, n + 1):
    sum = sum + x**i / i

# Display the final sum
print("Sum of the series =", sum)