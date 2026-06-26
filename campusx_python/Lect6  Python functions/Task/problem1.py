### `Problem-1:` Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Exercise 1:

# Input:[1,2,3,3,3,3,4,5]

# Output:[1, 2, 3, 4, 5]


def unique(y):
    s=set()
    for i in y:
        s.add(i)
    return list(s)
y=[1,2,3,3,3,3,4,5]
result=unique(y)
print(result)