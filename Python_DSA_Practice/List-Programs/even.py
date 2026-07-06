# ==========================================
# Program to Find All Even Numbers in a List
# ==========================================

# Create a list
a = [1, 2, 3, 4, 5, 6]

# Create an empty list to store even numbers
even = []

# Traverse each element in the list
for i in a:

    # Check if the current element is even
    if i % 2 == 0:
        # Add the even number to the new list
        even.append(i)

# Display the list of even numbers
print(f"The even numbers in the list are: {even}")

# Example:
# Original List: [1, 2, 3, 4, 5, 6]
#
# Output:
# The even numbers in the list are: [2, 4, 6]