# ==========================================
# Program to Read a CSV File and Display
# the First and Last Rows
# ==========================================

# Import the Pandas library
import pandas as pd

# Read the CSV file
df = pd.read_csv("output.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 Rows:")
print(df.tail())