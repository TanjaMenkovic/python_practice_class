class Flyable:
    def fly(self) -> None:
        print( "I can fly!")

class Swimmable:
    def swim(self) -> None:
        print( "I can swim!")

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly()  # Output: "I can fly!"
duck.swim()  # Output: "I can swim!"