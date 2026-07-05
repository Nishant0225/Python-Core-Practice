# ### `Problem-2:` Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.

# Example 1:

# Input:
# green-red-yellow-black-white

# Output:
# black-green-red-white-yellow
   
def sortedbhai(y):
    i=str(y).split("-")
    s="-".join(sorted(i))
    return s

y="green-red-yellow-black-white"
u=sortedbhai(y)
print(u)
    