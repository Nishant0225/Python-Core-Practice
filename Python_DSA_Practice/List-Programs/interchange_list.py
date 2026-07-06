# ==========================================
# Program to Swap the First and Last Elements
# of a List
# ==========================================

# Create a list
l = [1, 2, 3, 4, 5, 6]

# Store the first element in a temporary variable
temp = l[0]

# Replace the first element with the last element
l[0] = l[-1]

# Replace the last element with the original first element
l[-1] = temp

# Display the updated list
print(f"The list after swapping the first and last elements is: {l}")

# Example:
# Original List: [1, 2, 3, 4, 5, 6]
#
# Output:
# The list after swapping the first and last elements is:
# [6, 2, 3, 4, 5, 1]