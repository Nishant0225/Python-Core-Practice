# Write a program to Check if a given string is binary string of or not.
# A string is said to be binary if it's consists of only two unique characters.

# Take string input from user.

# Input: str = "01010101010"
# Output: Yes

# Input: str = "1222211"
# Output: Yes

# Input: str = "Campusx"
# Output: No

# A string is said to be binary if it contains only two unique characters.
# Take string input from user
i = input("Enter a string: ")

# Create an empty set to store unique characters
a = set()

# Traverse each character of the string
for b in i:
    a.add(b)

# Check whether exactly two unique characters are present
if len(a) == 2:
    print("The given string is binary string")
else:
    print("The given string is not binary string")