# ==========================================
# Program to Check Whether a Number is Prime
# ==========================================

# Take a number as input from the user
a = int(input("Enter a number: "))

# Assume the number is prime initially
is_prime = True

# Numbers less than or equal to 1 are not prime
if a <= 1:
    is_prime = False
else:
    # Check divisibility from 2 to a-1
    for i in range(2, a):
        # If the number is divisible by any value,
        # it is not a prime number
        if a % i == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print(f"{a} is a Prime Number.")
else:
    print(f"{a} is not a Prime Number.")

# Example:
# Input: 13
# Output: 13 is a Prime Number.