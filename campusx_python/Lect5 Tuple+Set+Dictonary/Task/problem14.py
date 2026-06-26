# Q4`: Convert a list of Tuples into Dictionary.
# Example 1:
# Input:
# ```bash
# [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
# ```
# Output:
# ```bash
# {'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}

# List of tuples (name, value)
l = [
    ("akash", 10),
    ("gaurav", 12),
    ("anand", 14),
    ("suraj", 20),
    ("akhil", 25),
    ("ashish", 30)
]

# Empty dictionary to store the result
d = {}

# Loop through each tuple in the list
for i in l:

    # i[0] -> name (key)
    # i[1] -> value
    # Store value inside a list as required in output
    d[i[0]] = [i[1]]

# Print the final dictionary
print(d)