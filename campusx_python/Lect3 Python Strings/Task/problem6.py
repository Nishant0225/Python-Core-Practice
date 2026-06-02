# Count the number of words in a string without using the split() function
# Example:
# Input  : "Hello how are you"
# Output : 4

# Take a string input from the user
a = input("Enter a string: ")

# Initialize word count to 1
# (Assuming the string contains at least one word)
count = 1

# Traverse through each character in the string
for i in a:
    # Increment the count whenever a space is encountered
    if i == " ":
        count += 1

# Display the total number of words
print("Number of words in string", a, "are:", count)

# Problem solved successfully