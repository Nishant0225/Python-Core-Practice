# Problem 10:
# Find all numbers between 2000 and 3200 (both included)
# that are divisible by 7 but not divisible by 5.
# Print the numbers in a single line separated by commas.
#
# Example Output:
# 2002,2009,2016,...

# Traverse through numbers from 2000 to 3200
for i in range(2000, 3200 + 1):

    # Check if the number is divisible by 7
    # and not divisible by 5
    if i % 7 == 0 and i % 5 != 0:

        # Print the number separated by commas
        print(i, end=",")

# Problem solved successfully