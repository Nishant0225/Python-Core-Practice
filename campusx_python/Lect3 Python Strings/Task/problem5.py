# Check whether a given string is a palindrome or not
# Example:
# Input  : "madam"
# Output : Palindrome

# Input  : "hello"
# Output : Not a Palindrome

# Take a string input from the user
a = input("Enter a string: ")

# Reverse the string using slicing
b = a[::-1]

# Compare the original string with its reverse
if a == b:
    print("The given string", a, "is a palindrome")
else:
    print("The given string", a, "is not a palindrome")

# Problem solved successfully