# abc - Abstract Base Class
from abc import ABC, abstractmethod


class Animal(ABC):  # В реальности мы не можем создать животное к-е просто животное.
    # ABC - указываем что такого класса быть самого по себе не может, он просто абстрактный.
    # Будет ошибка при создании экз. класса без переопределения abstract методов

    @abstractmethod  # Этим я указываю, что метод ОБЯЗАТЕЛЬНО должен быть переопределен во всех дочерних классах
    # (ошибки не будет, только подчеркивания в IDE, если нет наследования от ABC)
    def eat(self):
        pass


class Tiger(Animal):
    def eat(self):
        print("Tiger eats steak")


class Zebra(Animal):
    def eat(self):
        print("Zebra eats grass")


class Elephant(Animal):
    def elephant_eat(self):  # К примеру, другой разраб захотел унаследоваться от Animal.
        # Но в дочернем не переопределил метод, а написал свой
        print("Elephant eats peanuts")


class Penguin(Animal):
    def eating(self):  # Тоже кто-то определил свой, а не переопределил родительский
        print("Penguin is eating fish")


animal = Animal()  # Ошибка, так как класс наследуется от
# ABC Can't instantiate abstract class Animal with abstract method.
[animal.eat() for animal in (Tiger(), Zebra(), Elephant(), Penguin())]  # Tiger eats steak Zebra eats grass.
# В других мы не переопределили метод, а определили свой(к-й не вызвался), Как итог, вызвался родительский eat,
# к-й с pass в теле

# Чтобы этого избежать юзай декоратор abstractmethod
