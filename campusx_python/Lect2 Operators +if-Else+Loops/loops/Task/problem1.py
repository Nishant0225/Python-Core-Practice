# Problem 1:
# Use a for loop to print the following reverse number pattern:
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
#
# Each row starts from the row number and prints
# numbers in decreasing order up to 1.

a=int(input("Enter Rows"))

for i in range(a,0,-1):
    for j in range(i,0,-1):
        print(j,end="")

    print()