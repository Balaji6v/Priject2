class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

# Example usage:
dimensions = [5, 10]  # length and width
rect = Rectangle(dimensions[0], dimensions[1])
print(f"Area: {rect.area()}")       # Output: Area: 50
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 30
