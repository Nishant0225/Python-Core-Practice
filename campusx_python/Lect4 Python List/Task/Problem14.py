# Write a list comprehension that can transpose a given matrix
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

# Write a list comprehension to transpose a given matrix

# Given matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose matrix using list comprehension
L = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Print transposed matrix
print(L)