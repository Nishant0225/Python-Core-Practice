# ### `Problem 4:` Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def even(s):
    l=[]
    for i in s:
        if i%2==0:
            l.append(i)
    return list (l)

s=[1, 2, 3, 4, 5, 6, 7, 8, 9]
m=even(s)
print(m)