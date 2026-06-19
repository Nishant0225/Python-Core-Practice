# Problem 2:`Add new item to list after a specified item

# Write a program to add item 7000 after 6000 in the following Python List

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# Problem 2: Add new item to list after a specified item

# Given nested list
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Access the inner list [5000, 6000] using index positions
# list1[2] -> [300, 400, [5000, 6000], 500]
# list1[2][2] -> [5000, 6000]

# Append 7000 after 6000 in the inner list
list1[2][2].append(7000)

# Print the updated list
print(list1)