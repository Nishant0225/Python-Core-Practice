# Pattern 2: Write a program to print the following number pattern.

# Output:
# 1
# 121
# 12321
# 1234321

num=int(input('Enter Number of rows'))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
        
    
    print()
    