# Task 1
# Створіть абстрактний базовий клас "Фігура" і від нього успадкуйте конкретні класи, такі як "Коло", "Прямокутник", "Трикутник" і т.д. Кожен клас має мати методи для обчислення площі та периметру фігури. Створіть декілька об'єктів різних фігур і виведіть їх площу та периметр.A
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        ...

    @abstractmethod
    def square(self):
        ...


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return f"Rectangle\nP: {self.a + self.b + self.a + self.b};"

    def square(self):
        return f"S: {self.a * self.b};\n"


class Square(Figure):

    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return f"Square\nP: {4 * self.a};"

    def square(self):
        return f"S: {self.a * self.a};"


if __name__ == "__main__":
    x = Rectangle(2, 4)
    print(x.perimeter())
    print(x.square())

    y = Square(2)
    print(y.perimeter())
    print(y.square())