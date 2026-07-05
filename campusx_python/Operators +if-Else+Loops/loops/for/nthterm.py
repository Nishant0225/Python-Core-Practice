# Q4: Write a program to calculate the sum of the series:
# 1/1! + 2/2! + 3/3! + ... + n/n!
# where n is provided by the user.
import math
n=int(input("enter the nth term"))
temp=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    temp=temp+i/fact
    
print(temp)