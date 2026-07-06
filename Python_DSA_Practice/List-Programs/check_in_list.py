# ==========================================
# Program to Check Whether an Element
# Exists in a List
# ==========================================

# Create a list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Take the element to search from the user
d = int(input("Enter the element to search: "))

# ------------------------------------------
# Method 1: Using the 'in' Operator
# ------------------------------------------

# Check whether the element exists in the list
c = d in a

# ------------------------------------------
# Method 2: Using a for Loop
# ------------------------------------------

# Assume the element is not present
found = False

# Traverse the list
for i in a:
    # Check if the current element matches the search element
    if i == d:
        found = True
        break

# Display the result using the loop method
if found:
    print(f"{d} is present in the list (using loop).")
else:
    print(f"{d} is not present in the list (using loop).")

# Display the result using the 'in' operator
if c:
    print(f"{d} is present in the list (using 'in').")
else:
    print(f"{d} is not present in the list (using 'in').")

# Example:
# List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Input:
# 5
#
# Output:
# 5 is present in the list (using loop).
# 5 is present in the list (using 'in').