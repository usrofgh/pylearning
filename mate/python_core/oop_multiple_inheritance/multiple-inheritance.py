class Animal:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"{self.name} eats")


class Cat(Animal):
    def sleep(self):
        print(f"{self.name} sleeps")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")


class CatDog(Cat, Dog):  # Множественное наследование
    def laugh(self):
        print(f"{self.name} laughs")

kotopes = CatDog("Kotopes")
kotopes.eat()  # Animal
kotopes.sleep()  # Cat
kotopes.bark()  # Dog
kotopes.laugh()  # CatDog

print(dir(kotopes))
