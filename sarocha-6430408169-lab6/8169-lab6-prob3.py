import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius**2

    def perimeter_circle(self):
        return 2 * math.pi * self.radius

    @staticmethod
    def get_number(str):
        while True:
            try:
                number = float(input(str))
                return number
            except ValueError:
                print(f"Please enter a valid decimal number")


if __name__ == '__main__':
    radius = Circle.get_number("Enter a radius:")
    area = Circle(radius)
    print(
        f"The circle with radius {area.radius} has the area as {area.compute_area():.2f} and the perimeter as {area.perimeter_circle():.2f}")