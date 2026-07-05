# Q8: Given the first two terms of an Arithmetic Series, find the Nth term of the series. Assume all inputs are provided by the user.
a=int(input('Enter first term'))
b=int(input('Enter second term'))
n=int(input('Enter number of term'))
d=b-a
an=a + (n-1) * d
print("Nth term will be:",an)