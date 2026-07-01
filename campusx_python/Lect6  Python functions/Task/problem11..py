###`Problem 11:` Write a Python program to add three given lists using Python map and lambda.


x1=[1,2,3,4]
y1=[5,6,7,8]
z1=[9,10,11,12]

result=list(map(lambda x,y,z:x+y+z,x1,y1,z1))
print(result)

