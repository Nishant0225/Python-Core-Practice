# Write a program to print the following pattern
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

a=int(input("Enter range"))
for i in range(1,a+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
    
    