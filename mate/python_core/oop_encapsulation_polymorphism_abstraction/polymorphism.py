# Один интерфейс у классов, но различная реализация
len("eljl")
len([1, 2, 3])
# len работает по разному в зависимости от входящих аргументов

# Polymorphism:
add = lambda x, y, z=0: x + y + z
print(add(1, 2, 3))  # 6
print(add(1, 2))  # 3
# --------------


class USA:
    @staticmethod
    def print_type():
        print("USA is a developed country")

    @staticmethod
    def print_language():
        print("Primary language is English")


class India:
    @staticmethod
    def print_type():
        print("India is a eveloping country")

    @staticmethod
    def print_language():
        print("Primary language is Hindi")


obj_ind = India()
obj_usa = USA()

# По скольку у них общие методы, можем юзать for для всех, тоже полиморфизм
for country in (obj_ind, obj_usa):
    country.print_language()
    country.print_type()


# Ярче всего полиморфизм заметен при наследовании классов

class Animal:
    @staticmethod
    def breathe():
        print("Every animal is breathing, but:")

    def eat(self):
        print("Animal eats something")


class Cat(Animal):
    def eat(self):
        print("Cat drinks milk")


class Dog(Animal):
    def eat(self):
        print("Dog eats steak")


# Все животные дышит, у каждого есть свой рацион питания. Методы одни - реализация разная
[(animal.eat(), animal.breathe()) for animal in (Animal(), Cat(), Dog())]
# Animal eats something
# Every animal is breathing, but:
# Cat drinks milk
# Every animal is breathing, but:
# Dog eats steak
# Every animal is breathing, but:
