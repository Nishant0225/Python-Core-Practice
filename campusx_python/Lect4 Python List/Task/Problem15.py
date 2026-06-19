# Problem 15: Write a list comprehension that can flatten a nested list
# Input
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Problem 15: Flatten a nested list using list comprehension

# Given nested list (matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten the matrix into a single list
L = [j for i in matrix for j in i]

# Print result
print(L)