# Problem 15:Removal of all characters from a string except integers
# Given:

# str1 = 'I am 25 years and 10 months old'

# Expected Output:
# 2510


# Take string input from the user
str1 = input("Enter any string: ")

# String containing all digit characters
n = "0123456789"

# Empty string to store the extracted digits
ns = ""

# Traverse each character in the input string
for i in str1:

    # Check if the character is a digit
    if i in n:

        # Append the digit to the result string
        ns = ns + i

# Print the string containing only digits
print(ns)
    