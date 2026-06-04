# Determine whether a transaction results in profit, loss, or no profit/no loss
# Example:
# Cost Price    : 1000
# Selling Price : 1200
# Output        : Profit of 200

# Cost Price    : 1000
# Selling Price : 800
# Output        : Loss of 200

# Take cost price and selling price as input from the user
cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Selling Price: "))

# Check whether profit, loss, or no profit/no loss occurred
if sp > cp:
    print("Profit made of:", sp - cp)

elif cp > sp:
    print("Loss made of:", cp - sp)

else:
    print("No Profit No Loss")

# Problem solved successfully