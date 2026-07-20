# ==========================================
# Program to Perform Aggregation Functions
# in a Pandas DataFrame
# ==========================================

# Import the Pandas library
import pandas as pd

# Create a dictionary containing sample data
data = {
    "Name": ["Arun", "Varun", "Karun"],
    "Age": [28, 34, 22],
    "Salary": [10000, 20000, 30000]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# ------------------------------------------
# Calculate the average salary
# ------------------------------------------
avg_salary = df["Salary"].mean()
print("Average Salary:", avg_salary)

# ------------------------------------------
# Calculate the total salary
# ------------------------------------------
total_salary = df["Salary"].sum()
print("Total Salary:", total_salary)

# ------------------------------------------
# Find the minimum salary
# ------------------------------------------
min_salary = df["Salary"].min()
print("Minimum Salary:", min_salary)

# ------------------------------------------
# Find the maximum salary
# ------------------------------------------
max_salary = df["Salary"].max()
print("Maximum Salary:", max_salary)

# ------------------------------------------
# Calculate the average age
# ------------------------------------------
avg_age = df["Age"].mean()
print("Average Age:", avg_age)

# ------------------------------------------
# Find the minimum age
# ------------------------------------------
min_age = df["Age"].min()
print("Minimum Age:", min_age)

# ------------------------------------------
# Find the maximum age
# ------------------------------------------
max_age = df["Age"].max()
print("Maximum Age:", max_age)