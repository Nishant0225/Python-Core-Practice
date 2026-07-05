# Problem 14:Calculate the angle between the hour hand and minute hand.
# Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.
# Input:
# H = 9 , M = 0
# Output:
# 90
# Explanation:
# The minimum angle between hour and minute hand when the time is 9 is 90 degress.

# Problem 14: Calculate the minimum angle between
# the hour hand and minute hand.

# Take input from the user
h = int(input("Enter Hour: "))
m = int(input("Enter Minutes: "))

# If hour is 12, convert it to 0
if h == 12:
    h = 0

# Calculate the angle of the hour hand
hour_angle = (30 * h) + (0.5 * m)

# Calculate the angle of the minute hand
minute_angle = 6 * m

# Find the difference between the two angles
angle = abs(hour_angle - minute_angle)

# Find the smaller angle
if angle > 180:
    angle = 360 - angle

# Print the floor value of the angle
print("The angle between the hour and minute hand is:", int(angle))