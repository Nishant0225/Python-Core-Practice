# ==========================================
# Program to Create a DataFrame and
# Save it as CSV, Excel, and JSON Files
# ==========================================

# Import the Pandas library
import pandas as pd

# Create a dictionary containing sample data
data = {
    "Name": ["Ram", "Krushna", "Ganesh"],
    "Age": [10, 20, 30],
    "City": ["Ayodhya", "Vrundavan", "Gokuldham"]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# ==========================================
# Save the DataFrame as a CSV file
# index=False prevents row numbers from being saved
# ==========================================
df.to_csv("output.csv", index=False)

# ==========================================
# Save the DataFrame as an Excel file
# Requires openpyxl library
# ==========================================
df.to_excel("output.xlsx", index=False)

# ==========================================
# Save the DataFrame as a JSON file
# orient="records" stores each row as a JSON object
# ==========================================
df.to_json("output.json", orient="records", indent=4)

print("\nFiles created successfully:")
print("1. output.csv")
print("2. output.xlsx")
print("3. output.json")