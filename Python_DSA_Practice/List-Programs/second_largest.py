# ==========================================
# Program to Find the Second Largest Element
# in a List
# ==========================================

# Create a list
a = [1, 2, 3, 4, 5, 6, 7]

# Initialize variables to store the largest
# and second largest elements
m1 = m2 = 0

# Traverse the list
for i in a:

    # If the current element is greater than the largest element
    if i > m1:
        # Update the second largest element
        m2 = m1

        # Update the largest element
        m1 = i

    # If the current element is greater than the second largest
    # and not equal to the largest element
    elif i > m2 and i != m1:
        m2 = i

# Display the second largest element
print(f"The second largest element in the list is: {m2}")

# Example:
# List: [1, 2, 3, 4, 5, 6, 7]
#
# Output:
# The second largest element in the list is: 6