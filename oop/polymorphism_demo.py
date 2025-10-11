import math

# Base class
class Shape:
    def area(self):
        # This method must be overridden by any subclass
        raise NotImplementedError("Subclasses must override this method")


# Derived class for rectangles
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class for circles
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
