# Problem 12:Write a program to print whether a given number is a prime number or not
# Problem 12: Write a program to check whether a given number is prime or not.

# Take input from the user
a = int(input("Enter a number: "))

# Assume the number is prime (flag = 0)
flag = 0

# 0 and 1 are not prime numbers
if a <= 1:
    print(a, "is not a prime number")
else:
    # Check divisibility from 2 to a-1
    for i in range(2, a):
        # If the number is divisible by i, it is not prime
        if a % i == 0:
            flag = 1
            break   # Stop checking further

    # Print the result
    if flag == 1:
        print(a, "is not a prime number")
    else:
        print(a, "is a prime number")