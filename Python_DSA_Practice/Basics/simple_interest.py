# ==========================================
# Program to Calculate Simple Interest (SI)
# Formula: SI = (Principal × Rate × Time) / 100
# ==========================================

# Take the time period (in years) as input from the user
time = int(input("Enter the time (in years): "))

# Take the rate of interest (in percentage) as input
roi = int(input("Enter the rate of interest (%): "))

# Take the principal amount as input
p = int(input("Enter the principal amount: "))

# Calculate the Simple Interest using the formula
si = (p * roi * time) / 100

# Display the calculated Simple Interest
print(f"The Simple Interest is: {si}")

# Example:
# Input:
# Time = 2
# Rate = 5
# Principal = 10000
#
# Output:
# The Simple Interest is: 1000.0