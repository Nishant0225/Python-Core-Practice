# ### `Problem 3:` Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
# Expected Output :
# No. of Upper case characters :  9
# No. of Lower case Characters :  47

# Problem 3:
# Write a Python function that accepts a string and
# calculates the number of uppercase and lowercase letters.

def cou(i):
    # Variables to count uppercase and lowercase letters
    u = 0
    l = 0

    # Traverse each character in the string
    for j in i:

        # Check if character is uppercase
        if "A" <= j <= "Z":
            u += 1

        # Check if character is lowercase
        elif "a" <= j <= "z":
            l += 1

    # Return both counts
    return l, u


# Take input from the user
i = input("Enter a string: ")

# Function call
lower, upper = cou(i)

# Print the result
print("The number of lower case letters:", lower)
print("The number of upper case letters:", upper)