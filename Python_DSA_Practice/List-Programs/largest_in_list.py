# ==========================================
# Program to Find the Largest Element
# in a List
# ==========================================

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Find the largest element using the built-in max() function
print(f"The largest element using max() is: {max(numbers)}")

# Initialize the largest element with the first element of the list
lar = numbers[0]

# Traverse the list to find the largest element
for num in numbers:
    # Update 'lar' if the current element is greater
    if num > lar:
        lar = num

# Display the largest element
print(f"The largest element using a loop is: {lar}")

# Example:
# List: [1, 2, 3, 4, 5]
#
# Output:
# The largest element using max() is: 5
# The largest element using a loop is: 5