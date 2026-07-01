# ==========================================
# Mini ATM Project using OOP
# ==========================================

class Atm:

    # Constructor
    def __init__(self):
        # Instance variables
        self.pin = ''
        self.balance = 0

        # Automatically display the menu
        self.menu()

    # Menu Method
    def menu(self):

        user_input = input("""
Hi! How can I help you?

1. Press 1 to Create PIN
2. Press 2 to Change PIN
3. Press 3 to Check Balance
4. Press 4 to Withdraw Money
5. Press anything else to Exit

Enter your choice: """)

        if user_input == '1':
            self.create_pin()

        elif user_input == '2':
            self.change_pin()

        elif user_input == '3':
            self.check_balance()

        elif user_input == '4':
            self.withdraw()

        else:
            print("Thank you for using our ATM!")

    # Create PIN
    def create_pin(self):

        user_pin = input("Enter a new PIN: ")
        self.pin = user_pin

        user_balance = int(input("Enter Balance: "))
        self.balance = user_balance

        print("PIN created successfully.")

        self.menu()

    # Change PIN
    def change_pin(self):

        old_pin = input("Enter old PIN: ")

        if old_pin == self.pin:

            new_pin = input("Enter new PIN: ")
            self.pin = new_pin

            print("PIN changed successfully.")

        else:
            print("Wrong PIN!")

        self.menu()

    # Check Balance
    def check_balance(self):

        entered_pin = input("Enter PIN: ")

        if entered_pin == self.pin:
            print("Available Balance:", self.balance)
        else:
            print("Wrong PIN!")

        self.menu()

    # Withdraw Money
    def withdraw(self):

        entered_pin = input("Enter PIN: ")

        if entered_pin == self.pin:

            amount = int(input("Enter amount to withdraw: "))

            if amount <= self.balance:
                self.balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance:", self.balance)
            else:
                print("Insufficient Balance!")

        else:
            print("Wrong PIN!")

        self.menu()


# Creating an object
obj = Atm()