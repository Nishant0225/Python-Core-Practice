# Problem 1:
# Take a string as input from the user.
# Create a short form using the first letter of each word.
# Convert the short form to uppercase and print it.
#
# Example:
# Input:
# Data science mentorship program
#
# Output:
# DSMP

a=input("Enter a string")
b=a.title()
c=""
for i in b:
    if i>="A" and i<="Z":
        c=c+i
print(c)
        