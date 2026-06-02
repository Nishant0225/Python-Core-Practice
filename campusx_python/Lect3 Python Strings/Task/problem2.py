# Extract the username from a given email address
# Example:
# Input  : nitish24singh@gmail.com
# Output : nitish24singh

# Store the email address in a string variable
s = "nitish24singh@gmail.com"

# Find the position of '@' in the email address
position = s.index('@')

# Print the position of '@'
print(position)

# Extract and print the username (characters before '@')
print(s[0:position])