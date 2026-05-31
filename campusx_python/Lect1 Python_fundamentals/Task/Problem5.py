# Q5: Write a program to calculate Simple Interest by taking the principal amount, rate of interest, and time period as input from the user.
p=int(input('Enter Principal amount:'))
r=int(input('Enter Rate of Interest:'))
t=int(input('Enter Time Period'))
SI=((p*r*t)/100)
print("The simple interest will be :",SI)