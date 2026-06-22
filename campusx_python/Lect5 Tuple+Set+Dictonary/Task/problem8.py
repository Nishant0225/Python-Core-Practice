# Write a program to Check if a given string is binary string of or not.
# A string is said to be binary if it's consists of only two unique characters.

# Take string input from user.

# Input: str = "01010101010"
# Output: Yes

# Input: str = "1222211"
# Output: Yes

# Input: str = "Campusx"
# Output: No

# Write a program to check whether a given string is a binary string or not.
# A string is said to be binary if it contains only two unique characters.

# Take string input from user
i = input("Enter a string: ")

# Create an empty set to store unique characters
a = set()

# Traverse each character of the string
for b in i:

    # Add character to the set
    # Duplicate characters will be ignored automatically
    a.add(b)

# Check the number of unique characters
if len(a) > 2:

    # More than 2 unique characters
    print("The given string is not binary string")

else:

    # 2 or fewer unique characters
    print("The given string is binary string")