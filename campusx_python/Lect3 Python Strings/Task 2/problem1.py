# Take a string input from the user
a = input("Enter a string: ")

# Convert the first letter of each word to uppercase
b = a.title()

# Initialize an empty string to store the capital letters
c = ""

# Traverse through each character of the modified string
for i in b:

    # Check if the character is an uppercase letter (A-Z)
    if i >= "A" and i <= "Z":

        # Add the uppercase letter to the result string
        c = c + i

# Print the final string containing the first letter of each word
print(c)