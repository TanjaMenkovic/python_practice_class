from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> None:
        pass

class Dog(Animal):
    def make_sound(self) -> None:
        print("Aw Aw Aw... I'm a scary doggy... Woof!!!")

class Cat(Animal):
    def make_sound(self) -> None:
        print("Meeeeeeeeow... Feed me slave... Meeeeeow!!!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()