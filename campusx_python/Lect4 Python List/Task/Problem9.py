# Convert Character Matrix to single String using string comprehension.
# Example 1:

# Input:

# [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]

# Output:

# campux is best channel


# Convert Character Matrix to single String using string comprehension

# Given character matrix
a = [['c', 'a', 'm', 'p', 'u', 'x'],
     ['i', 's'],
     ['b', 'e', 's', 't'],
     ['c', 'h', 'a', 'n', 'n', 'e', 'l']]

# Step 1: convert each sublist into a word
words = [''.join([char for char in sublist]) for sublist in a]

# Step 2: join words with space
result = ' '.join(words)

# Print final result
print(result)