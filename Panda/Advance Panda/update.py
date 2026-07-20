# ==========================================
# Program to Update a Cell Using loc[]
# and Modify a Column in a Pandas DataFrame
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

# Update the 'Time' column at row index 0
# Since 'Time' does not exist, Pandas creates it.
df.loc[0, "Time"] = 10

# Add 10 to every value in the 'Time' column
# NaN + 10 remains NaN
df["Time"] = df["Time"] + 10

# Display the updated DataFrame
print("Updated DataFrame:")
print(df)

# Output:
#        Name  Age        City  Time
# 0       Ram   10    Ayodhya  20.0
# 1  Krushna   20  Vrundavan   NaN
# 2    Ganesh   30  Gokuldham  NaN