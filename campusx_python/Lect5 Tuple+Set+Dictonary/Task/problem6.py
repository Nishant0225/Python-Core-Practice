#  Write a program to find set of common elements in three lists using sets.
# Input : ar1 = [1, 5, 10, 20, 40, 80]
#         ar2 = [6, 7, 20, 80, 100]
#         ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Output : [80, 20]

# Write a program to find common elements in three lists using a set.

# Given lists
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Create an empty set to store common elements
c = set()

# Check elements of first list
for i in ar1:

    # If element is present in both second and third lists
    if i in ar2 and i in ar3:

        # Add it to the set
        c.add(i)

# Check elements of second list
for j in ar2:

    # If element is present in both first and third lists
    if j in ar1 and j in ar3:

        # Add it to the set
        c.add(j)

# Check elements of third list
for k in ar3:

    # If element is present in both first and second lists
    if k in ar1 and k in ar2:

        # Add it to the set
        c.add(k)

# Print the common elements
print(c)

