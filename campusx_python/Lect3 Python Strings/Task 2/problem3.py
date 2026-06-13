# Problem 13:
# Given a string containing both lowercase and uppercase letters,
# arrange the characters so that all lowercase letters come first,
# followed by all uppercase letters.

# Take string input from the user
str1 = input("Enter any string: ")

# Store uppercase letters
a = ""

# Store lowercase letters
b = ""

# Traverse each character in the string
for i in str1:

    # Check if the character is uppercase
    if i >= "A" and i <= "Z":
        a = a + i

    # Check if the character is lowercase
    elif i >= "a" and i <= "z":
        b = b + i

# Print lowercase letters first, then uppercase letters
print(b + a)