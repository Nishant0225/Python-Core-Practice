# Problem 1: Combine two lists index-wise (column-wise)

# Given two lists
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

# zip() combines elements from both lists based on their index
# List comprehension converts each tuple into a list
# Creates a new list containing paired elements index-wise
result = [list(item) for item in zip(list1, list2)]

# Print the final combined list
print(result)