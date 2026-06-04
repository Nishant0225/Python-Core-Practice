# Check whether three given angles can form a triangle or not
# Example:
# Angle 1 : 60
# Angle 2 : 60
# Angle 3 : 60
# Output  : Triangle can be formed

# Note:
# The sum of the three angles of a triangle must be 180 degrees.

# Take the three angles as input from the user
a = int(input("Enter First Angle: "))
b = int(input("Enter Second Angle: "))
c = int(input("Enter Third Angle: "))

# Check whether the sum of the three angles is 180 degrees
if (a + b + c == 180):
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")

# Problem solved successfully