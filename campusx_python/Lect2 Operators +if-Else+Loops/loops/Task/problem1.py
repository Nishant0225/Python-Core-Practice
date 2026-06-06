# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)
# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

# Take annual CTC (salary) as input from the user
a = int(input("Enter salary: "))

# Deduct HRA (10%), DA (5%), and PF (3%)
# Total deduction = 10% + 5% + 3% = 18%
ad = a - a * 0.18

# Check salary slab and apply tax accordingly

if a < 500000:
    # No tax for salary below 5 lakhs
    final = ad

elif a <= 1000000:
    # 10% tax for salary between 5 and 10 lakhs
    final = ad - (ad * 0.10)

elif a <= 2000000:
    # 20% tax for salary between 10 and 20 lakhs
    final = ad - (ad * 0.20)

else:
    # 30% tax for salary above 20 lakhs
    final = ad - (ad * 0.30)

# Convert annual in-hand salary to monthly salary
monthly_salary = final / 12

# Display the final monthly in-hand salary
print("Monthly in-hand salary is:", monthly_salary)