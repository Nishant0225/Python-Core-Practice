# ==========================================
# Program to Calculate Compound Interest (CI)
# Formula:
# Amount = Principal × (1 + Rate / 100) ^ Time
# Compound Interest = Amount - Principal
# ==========================================

# Take the principal amount as input from the user
p = float(input("Enter the Principal Amount: "))

# Take the annual rate of interest (in percentage)
r = float(input("Enter the Rate of Interest (%): "))

# Take the time period (in years)
t = float(input("Enter the Time (in years): "))

# Calculate the total amount after applying compound interest
amount = p * (1 + r / 100) ** t

# Calculate the Compound Interest
ci = amount - p

# Display the Compound Interest
print(f"The Compound Interest is: {ci:.2f}")

# Display the Total Amount
print(f"The Total Amount is: {amount:.2f}")

# Example:
# Input:
# Principal = 10000
# Rate = 10
# Time = 2
#
# Output:
# The Compound Interest is: 2100.00
# The Total Amount is: 12100.00