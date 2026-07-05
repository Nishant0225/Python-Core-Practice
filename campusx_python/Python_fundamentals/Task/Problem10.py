# Q10: Write a program to calculate the maximum number of glasses of milk that can be filled from a milk tank, given the dimensions of both the tank and the glass. Assume all dimensions are provided by the user.
h=int(input("Enter Height of milk tank"))
l=int(input("Enter length of milk tank"))
b=int(input("Enter breath of milk tank"))
gh=3
gr=1
voltank=l*b*h
volglass=3.14*gr**2
noofglass=voltank/volglass
print("Number of glasses that can be filled:", noofglass)