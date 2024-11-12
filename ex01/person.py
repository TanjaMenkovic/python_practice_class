class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def greet(self) -> None:
        print(f"Hello, my name is {self.name}.")

person1 = Person("Alice", 25)
person1.greet()  # Output: "Hello, my name is Alice."