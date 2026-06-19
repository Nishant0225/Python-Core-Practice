# Problem 8: Split String of list on K character.

# Example :

# Input:

# ['CampusX is a channel', 'for data-science', 'aspirants.']
# Output:

# ['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']

# Problem 8: Split String of list on K character

# Given list of strings
g = ['CampusX is a channel', 'for data-science', 'aspirants.']

# Empty list to store split words
n = []

# Loop through each string in the list
for i in g:
    
    # Split string into individual words
    words = i.split()
    
    # Add each word into result list
    for j in words:
        n.append(j)

# Print final list
print(n)