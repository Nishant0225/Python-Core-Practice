# Find list of common unique items from two list. and show in increasing order
# Input

# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]


# Given lists
num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]

# Empty list to store common elements
n = []

# Traverse through first list
for i in num1:
    
    # Check if element is present in second list
    if i in num2:
        n.append(i)

# Sort common elements in increasing order
n.sort()

# Print final result
print(n)