class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: "(4, 6)"    