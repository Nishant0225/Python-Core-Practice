# ==========================================
# CALLING A FUNCTION
# ==========================================

# Syntax:
# function_name(arguments)

# Example:

def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Calling the function inside a loop

for i in range(1, 11):
    x = is_even(i)
    print(x)

# Output:
# Odd
# Even
# Odd
# Even
# Odd
# Even
# Odd
# Even
# Odd
# Even