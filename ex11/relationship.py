class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower: int = horsepower

class Car:
    def __init__(self, make: str, engine: Engine) -> None:
        self.make: str = make
        self.engine: Engine = engine

    def show_details(self) -> None:
        print(f"Make: {self.make}, Engine Horsepower: {self.engine.horsepower}")

engine = Engine(200)
car = Car("Toyota", engine)
car.show_details()