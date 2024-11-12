class Vehicle:
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    def info(self) -> None:
        print(f"Make: {self.make}\nModel: {self.model}")

class Car(Vehicle):
    def __init__(self, make: str, model: str, seats: int) -> None:
        super().__init__(make, model)
        self.seats: int = seats

    def info(self) -> None:
        print(f"Make: {self.make}\nModel: {self.model}\nNumber of seats: {self.seats}")

car = Car("Toyota", "Corolla", 5)
car.info()  # Output: "Make: Toyota, Model: Corolla, Seats: 5"