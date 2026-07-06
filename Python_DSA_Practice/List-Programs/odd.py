# ==========================================
# Program to Find All Odd Numbers in a List
# ==========================================

# Create a list
a = [1, 2, 3, 4, 5, 6]

# Create an empty list to store odd numbers
odd = []

# Traverse each element in the list
for i in a:

    # Check if the current element is odd
    if i % 2 != 0:
        # Add the odd number to the new list
        odd.append(i)

# Display the list of odd numbers
print(f"The odd numbers in the list are: {odd}")

# Example:
# Original List: [1, 2, 3, 4, 5, 6]
#
# Output:
# The odd numbers in the list are: [1, 3, 5]