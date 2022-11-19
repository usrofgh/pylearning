# Память под переменные класса выделяется при создании первого экземпляра класса

class Dog:
    animal = "dog"

    def __init__(self, breed: str, color: str):
        self.breed = breed
        self.color = color

    def run(self):
        print('running')


hatiko = Dog("Akita", 'brown')
buzo = Dog("Bulldog", "black")

print(Dog.animal)  # dog
print(hatiko.animal)  # dog // сначала ищет в своих аттрибутах, потом переходит по аттрибуту __class__
# и дополнительно ищет там(уже в аттрибутах класса)
print(buzo.animal)  # dog

hatiko.animal = "cat"
print(hatiko.animal)  # cat // тут создается аттрибут экземпляра, так как нельзя ре-инициализировать аттрибут класса
print(buzo.animal)  # dog // тут по прежнему ссылается на аттрибут класса

Dog.run(hatiko)  # то же самое что и ниже, только ниже self(экз класса) подставляется автоматически
hatiko.run()  # ищем аттрибут(функцию) в аттрибутах экземпляра, не находим, переходим в аттрибут экз __class__ и ищем
# в аттрибутах классах. Тут метод - экземпляр класса
