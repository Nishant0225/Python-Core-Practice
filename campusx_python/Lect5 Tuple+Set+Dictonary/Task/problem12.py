# # `Q2`: Replace words from Dictionary. Given String, replace it’s words from lookup dictionary.
# # Example 1:
# # Input:
# # ```bash
# # test_str = 'CampusX best for DS students.'
# # repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
# # ```
# # Output:
# # ```bash
# # CampusX is the best channel for Data-Science students.

# Given string
test_str = 'CampusX best for DS students.'

# Dictionary containing words to replace
repl_dict = {
    "best": "is the best channel",
    "DS": "Data-Science"
}

# Split the string into words
words = test_str.split()

# List to store the modified words
result = []

# Traverse each word
for i in words:

    # If the word exists in the dictionary, replace it
    if i in repl_dict:
        result.append(repl_dict[i])

    # Otherwise, keep the original word
    else:
        result.append(i)

# Join all words into a single string
print(" ".join(result))
        
    
    
    