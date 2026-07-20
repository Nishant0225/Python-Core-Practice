# ==========================================
# Program to Fill Missing Values
# Using the Mean of a Column
# ==========================================

# Import the Pandas library
import pandas as pd

# Create a dictionary containing sample data
data = {
    "Name": ["Ram", "Krushna", "Ganesh", "Golu"],
    "Age": [10, 20, 30, None],
    "City": ["Ayodhya", "Vrundavan", "Gokuldham", None]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Replace missing values in the 'Age' column
# with the mean of the 'Age' column
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Display the updated DataFrame
print("Updated DataFrame:")
print(df)

# Output:
#       Name   Age        City
# 0      Ram  10.0    Ayodhya
# 1  Krushna  20.0  Vrundavan
# 2   Ganesh  30.0  Gokuldham
# 3     Golu  20.0       None