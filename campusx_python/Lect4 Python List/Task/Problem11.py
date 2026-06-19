# Write a program that can perform union operation on 2 lists
# Example:

# Input:

# [1,2,3,4,5,1]
# [2,3,5,7,8]
# Output:

# [1,2,3,4,5,7,8]

# Perform union operation on two lists (without duplicates)

# Given lists
a = [1, 2, 3, 4, 5, 1]
b = [2, 3, 5, 7, 8]

# List to store union result
c = []

# Add unique elements from first list
for i in a:
    if i not in c:
        c.append(i)

# Add unique elements from second list
for j in b:
    if j not in c:
        c.append(j)

# Print final union list
print(c)