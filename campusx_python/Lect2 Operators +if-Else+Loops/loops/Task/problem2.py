### Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

# Take the first angle as input from the user
a = int(input("Enter first angle: "))

# Take the second angle as input from the user
b = int(input("Enter second angle: "))

# Take the third angle as input from the user
c = int(input("Enter third angle: "))

# A triangle can be formed only if the sum of its three angles is 180 degrees
if a + b + c == 180:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")