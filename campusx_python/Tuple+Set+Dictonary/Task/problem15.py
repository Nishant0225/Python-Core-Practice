# Q5`: Sort Dictionary key and values List.
# Example 1:
# Input:
# ```bash
# {'c': [3], 'b': [12, 10], 'a': [19, 4]}
# ```
# Output:
# ```bash
# {'a': [4, 19], 'b': [10, 12], 'c': [3]}
# ```

a = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

d = {}

# Traverse keys in sorted order
for i in sorted(a):

    # Sort the value list and store it
    d[i] = sorted(a[i])

print(d)