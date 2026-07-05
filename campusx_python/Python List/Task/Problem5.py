# Problem 5:` You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.

# i.e. Say given list is [2,4,6,10,1]
# resultant list will be [22,20,10,23].

# For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.

# For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20

# like wise for all other elememts.

# [2,4,6,10,1]-->[22,20,16,10,23]


# Problem 5: Add all greater elements and itself for each element

# Given list
l1 = [2, 4, 6, 10, 1]

# Empty list to store resultant values
l2 = []

# Loop through each element in the list
for i in l1:
    
    # Variable to store sum of greater elements
    total = 0
    
    # Compare current element with every element in the list
    for j in l1:
        
        # Add elements which are greater than current element
        if i < j:
            total = total + j
    
    # Add current element itself to the total
    total = total + i
    
    # Store result in new list
    l2.append(total)

# Print final resultant list
print(l2)