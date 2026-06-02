# Remove a particular character from a given string
# Example:
# String    : "hello"
# Character : "l"
# Output    : "heo"

# Take a string input from the user
s = input("Enter a string: ")

# Take the character to be removed
e = input("Enter a character to remove: ")

# Traverse through each character in the string
for i in s:
    # Print the character only if it is not the one to be removed
    if e != i:
        print(i, end="")

# Problem solved successfully