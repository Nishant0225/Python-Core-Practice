# Problem 4: Menu-Driven Unit Converter

# Display the menu options
print("1. cm to ft")
print("2. km to miles")
print("3. USD to INR")
print("4. Exit")

# Take user's choice
choice = int(input("Enter your choice: "))

# Perform conversion based on user's choice
if choice == 1:
    # Convert centimeters to feet
    cm = float(input("Enter value in cm: "))
    ft = cm / 30.48
    print("Value in feet =", ft)

elif choice == 2:
    # Convert kilometers to miles
    km = float(input("Enter value in km: "))
    miles = km * 0.621371
    print("Value in miles =", miles)

elif choice == 3:
    # Convert USD to INR
    usd = float(input("Enter amount in USD: "))
    inr = usd * 86      # Approximate exchange rate
    print("Amount in INR =", inr)

elif choice == 4:
    # Exit the program
    print("Exiting Program...")

else:
    # Invalid menu choice
    print("Invalid Choice")