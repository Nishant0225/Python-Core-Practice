a=int(input("Enter a number"))
sum=0
b=0
while(a!=0):
    if(a>9):
        b=a%10
        a=a//10
        sum=sum+b
    else:
        sum=sum+a
        a=0
print(sum)