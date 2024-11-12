from datetime import date
from typing import Type, TypeVar

T = TypeVar('T', bound='Person')

class Person:
    def __init__(self, name: str, age: int, hobby: str = "nothing") -> None:
        self.name: str = name
        self.age: int = age
        self.hobby: str = hobby

    @classmethod
    def fromBirthYear(cls: Type[T], name: str, year: int) -> T:
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age: int) -> None:
        if age >= 18:
            print(f"Person whose age is {age} is an adult.")
        else:
            print(f"Person whose age is {age} isn't an adult.")

    def person_info(self) -> None:
        print(f"{self.name} is {self.age} years old and has a hobby: {self.hobby}.")

class Student(Person):
    def __init__(self, name: str, age: int, grade: int = 1) -> None:
        super().__init__(name, age)
        self.grade: int = grade

    def person_info(self) -> None:
        print(f"{self.name} is {self.age} years old and has a grade: {self.grade}.")

person1 = Person("Tanja", 32, "painting")
person2 = Person.fromBirthYear("Dalibor", 1991)
person2.hobby = "playing video games"

person1.person_info()
person2.person_info()

Person.isAdult(22)

person3 = Person.fromBirthYear("Alice", 1990)
person3.person_info()

student = Student.fromBirthYear("Bob", 2000)
student.person_info()