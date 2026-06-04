# Problem 3:
# Print the following pyramid star pattern:
#
#     *
#   * * *
# * * * * *
#
# Each row contains an odd number of stars.
# Print spaces before the stars to align the pattern
# in the shape of a pyramid.

a=int(input("Enter the row"))
b="*"
for i in range(1,a+1):
    for j in range(1,i,2):
        print(b*j,end="")
    print()