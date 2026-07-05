# Problem 19: Word location in String.
# Statement: Find a location of a word in a given sentence.

# Example 1:

# Input:
# Sentence: We can learn data science through campusx mentorship program.  
# word: campusx

# Output:
# Location of the word is 7.

# Note- Don't use index/find functions

# Problem 19: Word location in String
# Find the location (position) of a word in a given sentence
# without using index() or find() functions.

# Take the sentence as input
str1 = input("Enter string: ")

# Take the word to be searched
str2 = input("Enter word to find in string: ")

# Split the sentence into a list of words
s1 = str1.split()

# Variable to keep track of the word position
count = 0

# Flag variable to indicate whether the word is found
flag = 0

# Traverse each word in the list
for i in s1:

    # Check if the current word matches the search word
    if str2 == i:

        # Increment the position counter
        count += 1

        # Set the flag to indicate the word is found
        flag += 1

        # Exit the loop once the word is found
        break

    # Increment the position counter
    count += 1

# Check whether the word was found
if flag == 1:

    # Print the position of the word
    print("The word is at:", count, "spot")

else:

    # Print a message if the word is not found
    print("Word not found")
