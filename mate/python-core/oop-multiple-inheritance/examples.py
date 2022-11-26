class Transport:
    def __init__(self, position: str):
        self.position = position

    def travel(self, destination: str):
        print(f"Travel from {self.position} to {destination}")


class Car(Transport):
    pass


class Boat(Transport):
    pass


class Plane(Transport):
    pass

car = Car("Kyiv")
car.travel("Lviv")

boat = Boat("Left bank")
boat.travel("Right bank")

"""
Например мы хотим включать радиостанцию. Нужно реализовать метод, но где?
Transport - не подходит, от него наследуется лодка. там нет FM
"""