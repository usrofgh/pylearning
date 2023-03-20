import sys


class Car:
    def __init__(self, mark: str):
        self.mark = mark


car1 = Car("Car1")
car2 = Car("Car2")
car3 = Car("Car3")
print(sys.getrefcount(car1) - 1)
garage = [car1, car2]
print(sys.getrefcount(car1)- 1)

garage2 = garage
print(sys.getrefcount(car1)- 1)

house1 = [garage, car3]
print(sys.getrefcount(car1)- 1)

sys.getrefcount(car1)
print(sys.getrefcount(car1)- 1)

# Если так, то было бы намного больше число https://prnt.sc/glg0chTOx4aA