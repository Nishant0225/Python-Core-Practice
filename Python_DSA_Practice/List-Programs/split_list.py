# ==========================================
# Program to Split a List at a Given Position
# and Move the First Part to the End
# ==========================================

# Create a list
a = [1, 2, 3, 4, 5, 6]

# Take the split position as input from the user
d = int(input("Enter the split position: "))

# Handle cases where the split position is greater
# than the length of the list
d = d % len(a)

# Create an empty list to store the result
b = []

# Add elements from the split position to the end
b.extend(a[d:])

# Add elements from the beginning up to the split position
b.extend(a[:d])

# Display the updated list
print(f"The list after splitting at position {d} is: {b}")

# Example:
# Original List: [1, 2, 3, 4, 5, 6]
# Split Position: 2
#
# Output:
# The list after splitting at position 2 is:
# [3, 4, 5, 6, 1, 2]