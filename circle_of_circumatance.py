import math

class CircleConstructor:
    def __init__(self, radii):
        self.radii = radii

    def areas(self):
        return [math.pi * r**2 for r in self.radii]

    def circumferences(self):
        return [2 * math.pi * r for r in self.radii]

# Example usage
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circles = CircleConstructor(radii_list)

print("Areas:", circles.areas())
print("Circumferences:", circles.circumferences())
