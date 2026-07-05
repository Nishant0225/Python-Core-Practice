# Q7: Write a program to find the sum of squares of the first n natural numbers, where n is provided by the user.
n=int(input("Enter First n natural numbers"))
square=0
while(n>0):
    square=(n*n) + square
    n=n-1

print(square)