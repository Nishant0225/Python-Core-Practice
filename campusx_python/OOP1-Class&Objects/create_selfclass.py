# ==========================================
# Magic Method: __str__()
# ==========================================

# Definition:
# __str__() is a magic (dunder) method that returns a
# human-readable string representation of an object.
# It is automatically called when we use print(object).

class Fraction:

    # Parameterized Constructor
    def __init__(self, x, y):
        self.num = x      # Numerator
        self.den = y      # Denominator

    # Magic Method
    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    # Magic Method for Addition
    def __add__(self, other):
        pass


# Creating objects
f = Fraction(1, 2)

# Automatically calls __str__()
print(f)

# Output:
# 1/2