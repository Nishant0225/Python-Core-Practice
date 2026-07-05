# Q9: Given two fractions, find the sum of the fractions by taking the numerators and denominators as input from the user.
a=int(input("Enter Numerator of first fraction"))
b=int(input("Enter denominator of first fraction"))
c=int(input("Enter Numerator of second fraction"))
d=int(input("Enter Denominator of second fraction"))
sum=(a*d + b*c) / (b*d)
print("sum of fractions will be:",sum)