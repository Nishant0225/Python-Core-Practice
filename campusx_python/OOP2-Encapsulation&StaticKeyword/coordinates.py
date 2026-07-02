# ==========================================
# Finding Euclidean Distance Between Two Points
# ==========================================

# Definition:
# Euclidean distance is the shortest distance between two points.
#
# Formula:
# Distance = √((x₂ - x₁)² + (y₂ - y₁)²)

class Point:

    # Parameterized Constructor
    def __init__(self, x, y):
        self.x_cod = x      # X-coordinate
        self.y_cod = y      # Y-coordinate

    # Magic Method
    def __str__(self):
        return "<{}, {}>".format(self.x_cod, self.y_cod)

    # Method to calculate Euclidean Distance
    def euclidean_distance(self, other):

        return ((self.x_cod - other.x_cod) ** 2 +
                (self.y_cod - other.y_cod) ** 2) ** 0.5


# Creating objects
p1 = Point(0, 0)
p2 = Point(1, 2)

# Calling the method
print(p1.euclidean_distance(p2))

# Automatically calls __str__()
print(p1)

# Output:
# 2.23606797749979
# <0, 0>