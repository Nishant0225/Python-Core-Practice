# ==========================================
# Program to Check Whether an Array is
# Monotonic (Increasing or Decreasing)
# ==========================================

# Create a list
arr = [6, 5, 4, 4]

# Find the length of the list
n = len(arr)

# Check if the array is monotonically increasing
# Every element should be less than or equal to the next element
incr = all(arr[i] <= arr[i + 1] for i in range(n - 1))

# Check if the array is monotonically decreasing
# Every element should be greater than or equal to the next element
decr = all(arr[i] >= arr[i + 1] for i in range(n - 1))

# Display the result
print(f"Is the array monotonic? {incr or decr}")

# Example:
# List: [6, 5, 4, 4]
#
# Output:
# Is the array monotonic? True