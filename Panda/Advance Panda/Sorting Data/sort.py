# ==========================================
# Program to Sort a Pandas DataFrame
# by Single and Multiple Columns
# ==========================================

# Import the Pandas library
import pandas as pd

# Create a dictionary containing sample data
data = {
    "Name": ["Arun", "Varun", "Karun", "Tarun", "Rohit"],
    "Age": [28, 34, 22, 28, 22],
    "Salary": [10000, 20000, 30000, 25000, 15000]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# ------------------------------------------
# Sort by a Single Column (Age)
# ------------------------------------------

df1 = df.sort_values(by="Age", ascending=True)

print("\nSorted by Age (Ascending):")
print(df1)

# ------------------------------------------
# Sort by a Single Column (Age Descending)
# ------------------------------------------

df2 = df.sort_values(by="Age", ascending=False)

print("\nSorted by Age (Descending):")
print(df2)

# ------------------------------------------
# Sort by Multiple Columns
# Age -> Ascending
# Salary -> Descending
# ------------------------------------------

df3 = df.sort_values(
    by=["Age", "Salary"],
    ascending=[True, False]
)

print("\nSorted by Age (Ascending) and Salary (Descending):")
print(df3)

# ------------------------------------------
# Sort by Multiple Columns
# Age -> Descending
# Salary -> Ascending
# ------------------------------------------

df4 = df.sort_values(
    by=["Age", "Salary"],
    ascending=[False, True]
)

print("\nSorted by Age (Descending) and Salary (Ascending):")
print(df4)