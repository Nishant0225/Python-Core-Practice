# Problem 16: Check whether the string is Symmetrical.
# Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

# Example 1:

# Input
# khokho

# Output
# The entered string is symmetrical

# Take string input from the user
str1 = input("Enter any string: ")

# Find the length of the string
l = len(str1)

# Find the middle index of the string
a = l // 2

# Compare the first half and the second half of the string
if str1[:a] == str1[a:]:
    
    # If both halves are equal, the string is symmetrical
    print("Symmetrical")
else:
    
    # Otherwise, the string is not symmetrical
    print("Not Symmetrical")