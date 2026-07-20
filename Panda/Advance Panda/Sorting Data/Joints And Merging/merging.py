# ==========================================
# Program to Merge Two DataFrames
# Using Different Types of Joins
# ==========================================

# Import the Pandas library
import pandas as pd

# ------------------------------------------
# Create the Customer DataFrame
# ------------------------------------------
df_customers = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Ramesh", "Suresh", "Kalpesh"]
})

# ------------------------------------------
# Create the Orders DataFrame
# ------------------------------------------
df_orders = pd.DataFrame({
    "CustomerID": [1, 2, 4],
    "OrderAmount": [250, 450, 350]
})

# Display the original DataFrames
print("Customer DataFrame")
print(df_customers)

print("\nOrders DataFrame")
print(df_orders)

# ==========================================
# INNER JOIN
# Returns only matching records
# ==========================================
inner_df = pd.merge(
    df_customers,
    df_orders,
    on="CustomerID",
    how="inner"
)

print("\n========== INNER JOIN ==========")
print(inner_df)

# ==========================================
# LEFT JOIN
# Returns all rows from the left DataFrame
# ==========================================
left_df = pd.merge(
    df_customers,
    df_orders,
    on="CustomerID",
    how="left"
)

print("\n========== LEFT JOIN ==========")
print(left_df)

# ==========================================
# RIGHT JOIN
# Returns all rows from the right DataFrame
# ==========================================
right_df = pd.merge(
    df_customers,
    df_orders,
    on="CustomerID",
    how="right"
)

print("\n========== RIGHT JOIN ==========")
print(right_df)

# ==========================================
# OUTER JOIN
# Returns all rows from both DataFrames
# ==========================================
outer_df = pd.merge(
    df_customers,
    df_orders,
    on="CustomerID",
    how="outer"
)

print("\n========== OUTER JOIN ==========")
print(outer_df)