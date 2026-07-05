# Problem 18: Find uncommon words from two strings

# Take the first string as input
str1 = input("Enter first string: ")

# Take the second string as input
str2 = input("Enter second string: ")

# Split the first string into a list of words
s3 = str1.split()

# Split the second string into a list of words
s4 = str2.split()

# Empty list to store uncommon words
r = []

# Traverse words of the first string
for i in s3:

    # Check if the word is not present in the second string
    if i not in s4:

        # Add the word to the result list
        r.append(i)

# Traverse words of the second string
for i in s4:

    # Check if the word is not present in the first string
    if i not in s3:

        # Add the word to the result list
        r.append(i)

# Print the list of uncommon words
print(r)