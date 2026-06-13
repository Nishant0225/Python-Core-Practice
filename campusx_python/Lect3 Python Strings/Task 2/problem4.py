# Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.

# Input:
# hel123O4every093

# Output:
# Sum: 22
# Avg: 2.75

# Take string input from the user
str1 = input("Enter any string: ")

# Initialize variables to store the sum of digits
# and the count of digits
sum = 0
count = 0

# String containing all digit characters
n = "0123456789"

# Traverse each character of the input string
for i in str1:

    # Check whether the character is a digit
    if i in n:

        # Add the digit to the sum
        sum = sum + int(i)

        # Increase the count of digits
        count += 1

# Print the sum and average of the digits
print("Sum:", sum, "Avg:", sum / count)
    