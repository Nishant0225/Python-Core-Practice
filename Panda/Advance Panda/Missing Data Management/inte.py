# ==========================================
# Program to Fill Missing Numeric Values
# Using Linear Interpolation
# ==========================================

# Import the Pandas library
import pandas as pd

# Create a dictionary containing sample data
data = {
    "Name": ["Ram", "Krushna", "Ganesh", "Shritesh"],
    "Age": [10, 20, 30, None],
    "City": ["Ayodhya", "Vrundavan", "Gokuldham", None]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Fill missing numeric values using linear interpolation
df.interpolate(method="linear", axis=0, inplace=True)

# Display the updated DataFrame
print("Updated DataFrame:")
print(df)