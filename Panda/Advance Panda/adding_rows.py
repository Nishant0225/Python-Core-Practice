# ==========================================
# Program to Add and Insert Columns
# in a Pandas DataFrame
# ==========================================

# Import the Pandas library
import pandas as pd

# Create a dictionary containing sample data
data = {
    "Name": ["Ram", "Krushna", "Ganesh"],
    "Age": [10, 20, 30],
    "City": ["Ayodhya", "Vrundavan", "Gokuldham"]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Create a new column 'Newage'
# containing 10% of the Age values
df["Newage"] = df["Age"] * 0.1

# Insert a new column 'Time'
# at the first position (index 0)
df.insert(0, "Time", [1, 2, 3])

# Display the updated DataFrame
print("Updated DataFrame:")
print(df)

# Output:
#    Time      Name  Age        City  Newage
# 0     1       Ram   10    Ayodhya     1.0
# 1     2  Krushna   20  Vrundavan     2.0
# 2     3    Ganesh   30  Gokuldham    3.0