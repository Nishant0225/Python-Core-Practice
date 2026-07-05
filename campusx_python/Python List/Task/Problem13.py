# #  Write a list comprehension to print the following matrix
# # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# a = [[0, 1, 2],
#      [3, 4, 5],
#      [6, 7, 8]]

# Given matrix
a = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]

# Copy each row of matrix using list comprehension
l = [i for i in a]

# Print the matrix
print(l)