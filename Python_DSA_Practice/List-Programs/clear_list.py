# ==========================================
# Program to Clear All Elements from a List
# Using Two Different Methods
# ==========================================

# ------------------------------------------
# Method 1: Using the clear() Method
# ------------------------------------------

# Create a list
a = [1, 2, 3, 4, 5, 6, 7]

# Remove all elements from the list
a.clear()

# Display the empty list
print(f"List after using clear(): {a}")

# ------------------------------------------
# Method 2: Using the del Statement
# ------------------------------------------

# Create another list
b = [1, 2, 3, 4, 5, 6, 7]

# Delete all elements from the list using slicing
del b[:]

# Display the empty list
print(f"List after using del: {b}")

# Example:
# Original List: [1, 2, 3, 4, 5, 6, 7]
#
# Output:
# List after using clear(): []
# List after using del: []