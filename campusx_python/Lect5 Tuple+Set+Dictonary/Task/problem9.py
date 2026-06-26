# # Q4: find union of n arrays.
# # Example 1:

# # Input:

# # [[1, 2, 2, 4, 3, 6],
# #  [5, 1, 3, 4],
# #  [9, 5, 7, 1],
# #  [2, 4, 1, 3]]
# # Output:

# # [1, 2, 3, 4, 5, 6, 7, 9]

n = int(input("Enter number of arrays: "))

arr = []

for i in range(n):
    a = list(map(int, input(f"Enter array {i+1}: ").split()))
    arr.append(a)

s = set()

# Traverse each array
for i in arr:

    # Traverse each element of the array
    for j in i:
        s.add(j)

print(sorted(s))