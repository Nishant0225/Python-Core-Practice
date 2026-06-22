# Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.
# Input:

# Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
# Output:

# No of unique vowels-6

# Write a program to count the number of unique vowels in a string.
# Lowercase and uppercase vowels are considered different.

Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

# Create an empty set to store unique vowels
a = set()

# Traverse each character of the string
for i in Str1:

    # Check if the character is a vowel
    if i in "aeiouAEIOU":

        # Add the vowel to the set
        # Duplicate vowels will automatically be ignored
        a.add(i)

# Print the count of unique vowels
print("No of unique vowels =", len(a))