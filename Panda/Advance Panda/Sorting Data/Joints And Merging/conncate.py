# ==========================================
# Program to Concatenate DataFrames
# Using pd.concat()
# ==========================================

# Import the Pandas library
import pandas as pd

# ------------------------------------------
# Create the First DataFrame
# ------------------------------------------
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Ram", "Shyam", "Mohan"]
})

# ------------------------------------------
# Create the Second DataFrame
# ------------------------------------------
df2 = pd.DataFrame({
    "ID": [4, 5, 6],
    "Name": ["Raju", "Amit", "Rahul"]
})

print("First DataFrame")
print(df1)

print("\nSecond DataFrame")
print(df2)

# ==========================================
# Vertical Concatenation (axis=0)
# ==========================================

vertical_concat = pd.concat([df1, df2], axis=0)

print("\n========== Vertical Concatenation ==========")
print(vertical_concat)

# ==========================================
# Vertical Concatenation with New Index
# ==========================================

vertical_ignore = pd.concat(
    [df1, df2],
    axis=0,
    ignore_index=True
)

print("\n========== Vertical Concatenation (ignore_index=True) ==========")
print(vertical_ignore)

# ==========================================
# Horizontal Concatenation (axis=1)
# ==========================================

df3 = pd.DataFrame({
    "Age": [20, 21, 22]
})

horizontal_concat = pd.concat(
    [df1, df3],
    axis=1
)

print("\n========== Horizontal Concatenation ==========")
print(horizontal_concat)