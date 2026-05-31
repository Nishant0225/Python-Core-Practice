# Q4: Write a program to find the Euclidean distance between two coordinates by taking both coordinates as input from the user.

x1=float(input("enter x1:"))
x2=float(input("enter x2:"))
y1=float(input("enter y1:"))
y2=float(input("enter y2:"))


distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Euclidean Distance:", distance)