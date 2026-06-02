# Find the length of a given string without using the len() function

# Take string input from the user
s = input("Enter the string: ")

# Initialize a counter variable to store the length
count = 0

# Iterate through each character in the string
for i in s:
    # Increment the counter for every character
    count += 1

# Display the length of the string
print("Length of string is:", count)