# Calculate the in-hand monthly salary after deductions
# Deductions:
# HRA = 10% of CTC
# DA  = 5% of CTC
# PF  = 3% of CTC
#
# Tax Slabs:
# Below 5 Lakhs  -> 0%
# 5 to 10 Lakhs  -> 10%
# 10 to 20 Lakhs -> 20%
# Above 20 Lakhs -> 30%

# Take the annual CTC as input from the user
a = int(input("Enter the annual salary (CTC): "))

# Calculate HRA deduction (10% of CTC)
hra = (a / 100) * 10

# Calculate DA deduction (5% of CTC)
da = (a / 100) * 5

# Calculate PF deduction (3% of CTC)
pf = (a / 100) * 3

# Calculate salary after HRA, DA, and PF deductions
ab = a - (hra + da + pf)

# Apply tax based on the salary slab
if ab < 500000:
    final_salary = ab

elif ab <= 1000000:
    tax = (ab / 100) * 10
    final_salary = ab - tax

elif ab <= 2000000:
    tax = (ab / 100) * 20
    final_salary = ab - tax

else:
    tax = (ab / 100) * 30
    final_salary = ab - tax

# Calculate the monthly in-hand salary
monthly_salary = final_salary / 12

# Display the results
print("Annual in-hand salary:", final_salary)
print("Monthly in-hand salary:", monthly_salary)

# Problem solved successfully