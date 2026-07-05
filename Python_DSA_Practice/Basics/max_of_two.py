# ==========================================
# Program to Find the Greater of Two Numbers
# ==========================================

# Take the first number as input from the user
a = int(input("Enter the first number: "))

# Take the second number as input from the user
b = int(input("Enter the second number: "))

# Compare the two numbers
if a > b:
    # Executes if the first number is greater
    print(f"{a} is greater than {b}.")
else:
    # Executes if the second number is greater than or equal to the first
    print(f"{b} is greater than or equal to {a}.")