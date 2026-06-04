# Create a menu-driven program to perform unit and currency conversions
#
# Menu:
# 1. Centimeters (cm) to Feet (ft)
# 2. Kilometers (km) to Miles
# 3. USD to INR
# 4. Exit
#
# The user selects an option from the menu and enters the value
# to be converted. The program then displays the converted result.

# Take the value to be converted as input
a = float(input("Enter value to convert: "))

# Take the menu option from the user
t = int(input("Enter task number to perform:\n"
              "1. Centimeters (cm) to Feet (ft)\n"
              "2. Kilometers (km) to Miles\n"
              "3. USD to INR\n"
              "4. Exit\n"))

# Perform the selected operation
if t == 1:
    print("The converted value of", a, "cm is:", a / 30, "ft")

elif t == 2:
    print("The converted value of", a, "km is:", a * 1000)

elif t == 3:
    print("The converted value of", a, "USD is:", a * 95.65, "INR")

elif t == 4:
    print("Exiting program...")

else:
    print("Invalid choice")

# Problem solved successfully