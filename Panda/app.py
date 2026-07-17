# ==========================================
# Program to Read CSV, JSON, and Excel Files
# Using Pandas
# ==========================================

# Import the Pandas library
import pandas as pd

# ==========================================
# Read CSV File
# ==========================================

csv_df = pd.read_csv("teachers.csv")

print("========== CSV FILE ==========")
print(csv_df)


# ==========================================
# Read JSON File
# ==========================================

json_df = pd.read_json("sample_Data.json")

print("\n========== JSON FILE ==========")
print(json_df)


# ==========================================
# Read Excel File
# ==========================================

excel_df = pd.read_excel("SampleSuperstore.xlsx")

print("\n========== EXCEL FILE ==========")
print(excel_df)