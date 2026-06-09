# Problem 2: Print the following pattern.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

r=int(input("Enter range"))
if r%2==0:
    r+=1
s="*"
h=0
for i in range(1,r+1,2):
    for j in range(1,i+1,2):
        print(s,end="")
    print()
for a in range(r//2,0,-1):
    for b in range(a,0,-1):
        print(s,end="")
    print()
       
    