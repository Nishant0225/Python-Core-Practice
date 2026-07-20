# ==========================================
# Program to Delete a Column from
# a Pandas DataFrame
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

# Remove the 'Age' column permanently
# inplace=True modifies the original DataFrame
df.drop(columns=["Age"], inplace=True)

# Display the updated DataFrame
print("Updated DataFrame:")
print(df)

# Output:
# Updated DataFrame:
#        Name        City
# 0       Ram    Ayodhya
# 1  Krushna  Vrundavan
# 2    Ganesh  Gokuldham