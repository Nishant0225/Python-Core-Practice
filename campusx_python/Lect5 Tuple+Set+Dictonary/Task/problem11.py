# # Q1`: Key with maximum unique values
# # Given a dictionary with values list, extract key whose value has most unique values.
# # Example 1:
# # Input:
# # ```bash
# # test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
# # ```
# # Output:
# # ```bash
# # CampusX
# # ```

test_dict = {
    "CampusX": [5, 7, 9, 4, 0],
    "is": [6, 7, 4, 3, 3],
    "Best": [9, 9, 6, 5, 5]
}

max_unique = 0      # Stores maximum number of unique values
answer = ""         # Stores the key with maximum unique values

# Traverse each key in the dictionary
for key in test_dict:

    # Convert list into set to remove duplicates
    unique_values = set(test_dict[key])

    # Count unique values
    count = len(unique_values)

    # Update maximum and answer if current key has more unique values
    if count > max_unique:
        max_unique = count
        answer = key

# Print the required key
print(answer)