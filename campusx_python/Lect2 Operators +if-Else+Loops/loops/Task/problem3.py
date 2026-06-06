# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

# Take cost price as input from the user
cp = int(input("Enter Cost Price: "))

# Take selling price as input from the user
sp = int(input("Enter Selling Price: "))

# Check whether there is a profit, loss, or no profit/no loss
if sp > cp:
    print("Profit : Rs.", sp - cp)

elif cp > sp:
    print("Loss : Rs.", cp - sp)

else:
    print("No Profit No Loss")