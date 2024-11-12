class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

rect = Rectangle(4, 5)
print(rect.area)  # Output: 20
print(rect.perimeter)  # Output: 18    