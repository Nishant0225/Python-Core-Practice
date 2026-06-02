# Count the frequency of a particular character in a given string
# Example:
# String    : "hello how are you"
# Character : 'h'
# Output    : 2

# Take a string input from the user
s = input("Enter a string: ")

# Take the character whose frequency is to be counted
a = input("Enter a character: ")

# Initialize a counter variable
count = 0

# Traverse through each character in the string
for i in s:
    # Check if the current character matches the given character
    if i == a:
        count += 1

# Display the frequency of the character
print("The character", a, "appears", count, "time(s) in the string.")