# ==========================================
# Program to Check Missing Values
# in a Pandas DataFrame
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

# Check for missing (NULL/NaN) values
# True  -> Missing value present
# False -> Value is present
print("Missing Values:")
print(df.isnull())

# Output:
# Missing Values:
#     Name    Age   City
# 0  False  False  False
# 1  False  False  False
# 2  False  False  False
# 3  False   True   True