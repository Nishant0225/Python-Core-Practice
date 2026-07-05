# Write a program that can find the max number of each row of a matrix
# Example:

# Input:

# [[1,2,3],[4,5,6],[7,8,9]]
# Output:

# [3,6,9]

# Find maximum number of each row in a matrix

# Given matrix
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# List to store maximum of each row
m = []

# Loop through each row in matrix
for i in a:
    
    # Find maximum value in current row and append to result
    m.append(max(i))

# Print final result
print(m)
    

