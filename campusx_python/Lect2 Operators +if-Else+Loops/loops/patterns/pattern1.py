# Q1: Write a program to print the following star pattern using nested loops:

# *
# **
# ***

num=int(input('Enter Number of rows'))
a='*'
for i in range(1,num+1):
    print(a*i)
    