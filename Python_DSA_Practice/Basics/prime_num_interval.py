# ==========================================
# Program to Find Prime Numbers in a Given Range
# Using the Sieve of Eratosthenes Algorithm
# ==========================================

# Define the starting and ending values of the range
x, y = 2, 7

# Create a list assuming all numbers are prime initially
# Index represents the number, and the value (True/False)
# indicates whether it is prime.
primes = [True] * (y + 1)

# 0 and 1 are not prime numbers
primes[0] = False
primes[1] = False

# Apply the Sieve of Eratosthenes algorithm
# Iterate up to the square root of the upper limit
for i in range(2, int(y ** 0.5) + 1):

    # If the current number is prime
    if primes[i]:

        # Mark all multiples of 'i' as non-prime
        # Start from i² because smaller multiples
        # have already been processed.
        for j in range(i * i, y + 1, i):
            primes[j] = False

# Create a list of prime numbers within the given range
res = [i for i in range(x, y + 1) if primes[i]]

# Display the result
print(f"Prime numbers between {x} and {y}: {res}" if res else "No prime numbers found.")

# Example:
# Range: 2 to 7
# Output:
# Prime numbers between 2 and 7: [2, 3, 5, 7]