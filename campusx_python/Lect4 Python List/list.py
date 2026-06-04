# ==============================
# Characteristics of a List
# ==============================

# 1. Ordered
# Elements are stored in a specific order and maintain that order.

fruits = ["apple", "banana", "mango"]
print(fruits[0])  # Output: apple


# 2. Mutable (Changeable)
# List elements can be modified after creation.

fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'mango']


# 3. Heterogeneous
# A list can store different data types together.

data = [10, "Python", 3.14, True]
print(data)


# 4. Allows Duplicates
# Duplicate values are permitted in a list.

numbers = [1, 2, 2, 3, 3, 3]
print(numbers)


# 5. Dynamic
# Elements can be added or removed at runtime.

numbers.append(4)
print(numbers)

numbers.remove(2)
print(numbers)


# 6. Supports Nesting
# A list can contain other lists.

nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1])      # Output: [3, 4]
print(nested_list[1][0])   # Output: 3


# 7. Accessible by Index
# Elements can be accessed using their position.

colors = ["red", "green", "blue"]
print(colors[2])  # Output: blue


# 8. Can Store Any Python Object
# Lists can store strings, numbers, dictionaries, tuples, functions, etc.

sample = [
    10,
    "Hello",
    (1, 2),
    {"name": "Nishant"},
    [5, 6, 7]
]
print(sample)

# Adding Item in list
 
# Append
S=[1,2,3,4,5,6,7]
S.append(6)
print(S)

# Insert 
R=[1,2,3,4,5,6,7]
R.insert(1,100)
print(R)

# Editing the items in list 
O=[1,2,3,4,5,6,7]
O[0:3]=[100,200,300,400,500]
print(O)

# Deleting items from list 

# del 
O=[1,2,3,4,5,6,7]
del O

# slicing

J=[1,2,3,4,5,6,7]
del J[0]
print(J)

H=[1,2,3,4,5,6,7]
del H[0:3]
print(H)

# Remove
D=[1,2,3,4,5,6,7]
D.remove(5)
print(D) 

# Pop 
C=[1,2,3,4,5,6,7]
C.pop()
print

#clear
f=[1,2,3,4,5,6,7]
f.clear()

# Operations on List

# Arithmetic Operations
a=[1,2,3,4,5,6,7]
a=[1,2,3,4,5,6,7]
b=[8,9,10,11,12,13]
print(a+b)
print(a*3)

# Loops in List 
z=[1,2,3,4,5,6,7]
for i in z:
    print(i)

# Funtions in list

# len 
aa=[1,2,3,4,5,6,7]
print(len(aa))
print(min(aa))
print(max(aa))
print(sorted(aa))
print(sorted(aa),reversed=True)
aa.count(4)

# ==============================
# Summary
# ==============================
# ✓ Ordered
# ✓ Mutable
# ✓ Heterogeneous
# ✓ Allows Duplicates
# ✓ Dynamic
# ✓ Supports Nesting
# ✓ Accessible by Index
# ✓ Can Store Any Python Object