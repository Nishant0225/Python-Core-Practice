# Write a program to print the following pattern
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

a=int(input("Enter range"))
for i in range(1,a+1):
    for j in range(1,i+1):
        for k in range(j,0,-1):
            print(k,end="")
        print()
    