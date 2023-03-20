class Animal:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"{self.name} eats")


class Cat(Animal):
    def sleep(self):
        print(f"{self.name} sleeps")

    def eat(self):
        print(f"{self.name} drinks milk")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

    def eat(self):
        print(f"{self.name} eats steak")


class CatDog(Cat, Dog):  # Множественное наследование
    def laugh(self):
        print(f"{self.name} laughs")

cat = Cat("cat")
dog = Dog("dog")

cat.eat()  # cat drinks milk
dog.eat()  # dog eats steak

kotopes = CatDog("Kotopes")
kotopes.sleep()  # Cat
kotopes.bark()  # Dog
kotopes.laugh()  # CatDog
#  В целом лучше не допускать таких ситуаций, пользоваться им только когда методы классов не повторяются
kotopes.eat()  # Kotopes drinks milk // Зависит от того, какой класс указан 1-м в наследовании - MRO.

print(CatDog.mro())  # отображает порядок обращения к классам.
# Нет в текущем классе нужного метода? Идет к другому - по списку
# [<class '__main__.CatDog'>, <class '__main__.Cat'>,
# <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>]
