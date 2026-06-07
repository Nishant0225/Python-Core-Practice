# Loop through all numbers from 2000 to 3200 (inclusive)
for i in range(2000, 3201):

    # Check if the number is divisible by 7
    # and not divisible by 5
    if i % 7 == 0 and i % 5 != 0:

        # Print the number followed by a comma
        # end="" prevents printing on a new line
        print(i, ",", end="")