# ==========================================
# Program to Check Whether a Number is an
# Armstrong Number or Not
# ==========================================

# Take a number as input from the user
a = int(input("Enter a number: "))

# Store the original number for comparison later
original_num = a

# Variable to store the sum of powered digits
sum = 0

# Count the number of digits in the given number
n = len(str(a))

# Extract each digit and calculate the sum of its powers
while a > 0:
    # Get the last digit
    digit = a % 10

    # Add digit raised to the power of total digits
    sum += digit ** n

    # Remove the last digit
    a = a // 10

# Check whether the number is an Armstrong number
if sum == original_num:
    print(f"{original_num} is an Armstrong Number.")
else:
    print(f"{original_num} is not an Armstrong Number.")

# Example:
# Input: 153
# Output: 153 is an Armstrong Number.