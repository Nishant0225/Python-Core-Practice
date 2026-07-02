# ==========================================
# Method Overriding in Python
# ==========================================

# Definition:
# Method Overriding is an OOP concept where a child class
# provides its own implementation of a method that already
# exists in the parent class.

# It represents Runtime Polymorphism.

# Rules:
# • Parent and Child methods must have the same name.
# • Parameters should also be the same.
# • Child method overrides the Parent method.

# Advantages:
# • Customizes the inherited method.
# • Increases code flexibility.
# • Supports Runtime Polymorphism.


# ==========================================
# Parent Class
# ==========================================

class Phone:

    # Constructor
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")

        self.__price = price      # Private Attribute
        self.brand = brand
        self.camera = camera

    # Parent Method
    def buy(self):
        print("Buying a Phone")

    # Getter Method
    def get_price(self):
        return self.__price


# ==========================================
# Child Class
# ==========================================

class SmartPhone(Phone):

    # Overriding Parent Method
    def buy(self):
        print("Buying a SmartPhone")


# ==========================================
# Creating Object
# ==========================================

s = SmartPhone(20000, "Apple", 13)


# ==========================================
# Calling Overridden Method
# ==========================================

s.buy()


# ==========================================
# Accessing Parent Attributes
# ==========================================

print("\nBrand  :", s.brand)
print("Camera :", s.camera)

# Accessing Private Attribute using Getter
print("Price  :", s.get_price())


# ==========================================
# Output
# ==========================================

# Inside Phone Constructor
# Buying a SmartPhone
#
# Brand  : Apple
# Camera : 13
# Price  : 20000


# ==========================================
# Short Notes
# ==========================================

# Method Overriding:
# Method Overriding is the process of redefining
# a method in the child class that already exists
# in the parent class.

# Rules:
# • Method name must be the same.
# • Parameters should be the same.
# • Child method executes instead of Parent method.

# Method Resolution Order (MRO):
# Child Class → Parent Class → object

# Advantages:
# • Customizes inherited methods.
# • Supports Runtime Polymorphism.
# • Improves flexibility and reusability.