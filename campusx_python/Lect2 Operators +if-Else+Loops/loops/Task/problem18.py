# Problem 3 :Write a program to pring the following pattern

#         *
#       * * *
#     * * * * *
#    * * * * * * *
# * * * * * * * * *

r=int(input("Enter range"))
for i in range(1,r+1):
    for j in range(1,r-i+1):
        print(" ", end=" ")
    for s in range(2*i-1):
        print("*",end=" ")
    print()
        
        