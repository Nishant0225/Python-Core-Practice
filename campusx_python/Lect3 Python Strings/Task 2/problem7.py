# roblem 17: Reverse words in a given String

# Statement: We are given a string and we need to reverse words of a given string.

# Example 1:

# Input:
# geeks quiz practice code

# Output:
# code practice quiz geeks

# Example 2:

# Input:
# my name is laxmi

# Output:
# laxmi is name my

# Take string input from the user
str1 = input("Enter any string: ")

# Split the string into a list of words
s = str1.split()

# Find the number of words in the list
l = len(s)

# Reverse the list of words
a = s[l::-1]

# Traverse the reversed list and print each word
for i in a:

    # Print each word followed by a space
    print(i, " ", end="")