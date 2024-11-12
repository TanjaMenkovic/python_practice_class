from typing import Type, TypeVar

T = TypeVar('T', bound='MathOperations')

class MathOperations:
    @staticmethod
    def add(num1: int, num2: int) -> int:
        return num1 + num2

    @classmethod
    def describe(cls: Type[T]) -> str:
        return "This class provides basic math operations."

print(MathOperations.add(5, 3))  # Output: 8
print(MathOperations.describe())  # Output: "This class provides basic math operations."

    