class Circle:
    # Private class variable
    __pi = 3.141

    def __init__(self, radius):
        self.radius = radius  # Public instance variable

    def calculate_area(self):
        # Use the private class variable __pi
        return Circle.__pi * (self.radius ** 2)

    def calculate_circumference(self):
        # Use the private class variable __pi
        return 2 * Circle.__pi * self.radius

