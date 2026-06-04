# Problem 7: Reverse a Given Integer Number
#
# Write a program that takes an integer as input
# and prints the number with its digits reversed.
#
# Example:
# Input:
# 76542
#
# Output:
# 24567
#
# Explanation:
# The digits of 76542 are reversed to form 24567.

a=int(input("Enter an number"))
temp=0
i=9
while a<=10:
    temp=temp+a%10
    a=a/10
    print(a)
print(temp)
    