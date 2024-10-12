import math


class Shape:
    # Define the base class

    def area(self):
        # Method to calculate the area respective
        raise NotImplementedError(
            "The drived classes need to override this method")


class Rectangle(Shape):
    # Define a drived class
    def __init__(self, length, width):
        super().__init__()
        # Inherits from shape class

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()

        self.raduis = radius

    def area(self):

        return math.pi * (self.radius ** 2)
