# Problem 3 :Write a program to pring the following pattern

#         *
#       * * *
#     * * * * *
#    * * * * * * *
# * * * * * * * * *

a=int(input("Enter range"))

for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
        
        
        