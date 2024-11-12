import math

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius: float = radius
    
    def area(self) -> float:
        return self.radius ** 2 * math.pi

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

circle1 = Circle(5)
print(circle1.area())  # Output: 78.54 (approximately)
print(circle1.circumference())  # Output: 31.42 (approximately)