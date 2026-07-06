# ==========================================
# Program to Find the Length of a List
# ==========================================

# Create a list
a = [1, 2, 3, 4, 5, 6, 7, 8]

# -------------------------------
# Method 1: Using the len() Function
# -------------------------------

# Find the length of the list using the built-in len() function
print(f"The length of the list using len() is: {len(a)}")

# -------------------------------
# Method 2: Using a for Loop
# -------------------------------

# Initialize a counter variable
count = 0

# Traverse each element in the list
for i in a:
    # Increase the counter by 1 for each element
    count += 1

# Display the length of the list
print(f"The length of the list using a loop is: {count}")

# Example:
# List: [1, 2, 3, 4, 5, 6, 7, 8]
#
# Output:
# The length of the list using len() is: 8
# The length of the list using a loop is: 8