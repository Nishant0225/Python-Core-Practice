# Problem 3:Update no of items available

# Suppose you are given a list of candy and another list of same size representing no of items of respective candy. 

# i.e - 
# candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
# no_of_items = [10,20,34,74,32]

# Write a program to show no. of items of each candy type.

# Output:
# Jelly Belly-10
# Kit Kat-20
# Double Bubble-34
# Milky Way-74
# Three Musketeers-32

# Problem 3: Update number of items available

# List containing candy names
candy_list = ['Jelly Belly', 'Kit Kat', 'Double Bubble', 'Milky Way', 'Three Musketeers']

# List containing number of items available for each candy
no_of_items = [10, 20, 34, 74, 32]

# zip() combines candy names and their quantities index-wise
# Convert each tuple into a list
result = [list(item) for item in zip(candy_list, no_of_items)]

# Print candy name with its available quantity
for i in result:
    print(i[0], "-", i[1])