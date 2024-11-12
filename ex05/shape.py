import math
from typing import List

class Shape:
    def area(self) -> float:
        raise NotImplementedError("This method can't be implemented from base class.")

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height
    
    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius: float = radius
    
    def area(self) -> float:
        return self.radius ** 2 * math.pi

try:
    shapes: List[Shape] = [Rectangle(4, 5), Circle(3), Shape()]
    for shape in shapes:
        print(shape.area())
except NotImplementedError:
    print("Oops! Can't access. Try again...")
