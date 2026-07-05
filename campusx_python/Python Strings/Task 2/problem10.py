# Problem 20:
# Write a program to remove all duplicate characters from a string.

# Take string input from the user
str1 = input("Enter string: ")

# Empty string to store characters without duplicates
k = ""

# Traverse each character of the input string
for i in str1:

    # Check if the character is not already present
    # in the result string
    if i not in k:

        # Add the character to the result string
        k = k + i

# Print the string after removing duplicate characters
print(k)