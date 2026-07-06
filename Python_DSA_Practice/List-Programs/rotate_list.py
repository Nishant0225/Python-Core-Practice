# ==========================================
# Program to Rotate a List to the Left
# by 'd' Positions
# ==========================================

# Create a list
l = [1, 2, 3, 4, 5]

# Take the number of left rotations as input from the user
d = int(input("Enter the number of rotations: "))

# Handle cases where the rotation count is greater than the list length
# Example: Rotating a list of length 5 by 7 positions is the same as rotating it by 2 positions.
d = d % len(l)

# Perform the left rotation using list slicing
rotated_list = l[d:] + l[:d]

# Display the rotated list
print(f"The list after {d} left rotation(s) is: {rotated_list}")

# Example:
# Original List: [1, 2, 3, 4, 5]
# Rotations: 2
#
# Output:
# The list after 2 left rotation(s) is: [3, 4, 5, 1, 2]