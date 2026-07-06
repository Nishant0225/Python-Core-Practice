# ==========================================
# Remove Duplicates Using a New List
# ==========================================

a = [1, 2, 2, 1, 3, 4, 5, 6, 7, 8]

unique = []

for num in a:
    if num not in unique:
        unique.append(num)

print(f"The list after removing duplicate elements is: {unique}")