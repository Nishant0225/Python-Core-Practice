# ==========================================
# Program to Remove Multiple Elements
# from a List
# ==========================================

# Create the original list
a = [10, 20, 30, 40, 50, 60, 70]

# Create a list containing the elements to be removed
remove = [20, 40, 60]

# Create a new list by keeping only those elements
# that are not present in the 'remove' list
a = [x for x in a if x not in remove]

# Display the updated list
print(f"The list after removing the specified elements is: {a}")

# Example:
# Original List: [10, 20, 30, 40, 50, 60, 70]
# Elements to Remove: [20, 40, 60]
#
# Output:
# The list after removing the specified elements is:
# [10, 30, 50, 70]