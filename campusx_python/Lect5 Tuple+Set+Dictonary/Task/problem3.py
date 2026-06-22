# Check is tuples are same or not?
# Two tuples would be same if both tuples have same element at same index

# t1 = (1,2,3,0)
# t2 = (0,1,2,3)

# t1 and t2 are not same

a = (1,2,3,0)
b = (0,1,2,3)
d=0
flag=0
for i in a:
        if i!=b[d]:
            flag+=1
        d+=1    
if flag>0 and len(a)!=len(b):
    print("The string is not same")
else:
    print("The string is same")
