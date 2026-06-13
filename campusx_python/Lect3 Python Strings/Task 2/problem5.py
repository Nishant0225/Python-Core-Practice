# Problem 15:Removal of all characters from a string except integers
# Given:

# str1 = 'I am 25 years and 10 months old'

# Expected Output:
# 2510

str1 = input("Enter any string: ")
n="0123456789"
ns=""
for i in str1:
    if i in n:
        ns=ns+i
print(ns)
    