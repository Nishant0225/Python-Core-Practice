# Problem 4:Running Sum on list
# Write a program to print a list after performing running sum on it.

# i.e:
# Input:
# list1 = [1,2,3,4,5,6]

# Output:
# [1,3,6,10,15,21]

list1 = [1,2,3,4,5,6]
# Problem 4: Running Sum on list

# Given list
list1 = [1, 2, 3, 4, 5, 6]

# Create an empty list to store running sum values
l2 = []

# Variable to store current sum
total = 0

# Loop through each element in the list
for i in list1:
    # Add current element to total sum
    total = total + i
    
    # Add updated sum to new list
    l2.append(total)

# Print the running sum list
print(l2)