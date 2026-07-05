# Problem-7 Write a python function that accepts a string as input and returns the word with most occurence.

# Input:
# hello how are you i am fine thank you

# Output
# you -> 2

# Problem-7: Find the word with the maximum occurrence

def mostt(a):

    # Split the string into words
    b = a.split()

    # Store maximum count
    max_count = 0

    # Store the word with maximum occurrence
    m = ""

    # Traverse each word
    for i in b:

        # Count occurrences of the current word
        count = b.count(i)

        # Update if current word has a higher count
        if count > max_count:
            max_count = count
            m = i

    # Return the word and its count
    return m, max_count


# Take input from the user
a = input("Enter a string: ")

# Function call
q, p = mostt(a)

# Print the result
print(q, "->", p)