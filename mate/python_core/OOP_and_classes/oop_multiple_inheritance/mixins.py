class Transport:
    def __init__(self, position: str) -> None:
        self.position = position

    def travel(self, destination: str) -> None:
        print(f"Travel from {self.position} to {destination}")


class Car(Transport):
    @staticmethod
    def play_song_on_station(station) -> None:
        print(f"Play song on station {station}!")


class Boat(Transport):
    pass

car = Car('Kiev')
car.play_song_on_station("FM")  # Тут всё логично
boat = Boat("Kiev")

# boat.play_song_on_station("FM")  # не запущу, нет такого. Если перенести функцию радио в Transport,
# то будет глупо если у Boat, будет этот метод. Если создать отдельный класс Phone, то придется копипастить.
# Выход - расширение функционала определенного класса путем наследования - Mixin


class RadioUserMixin:  # функционал этого класса отсутствует в базовом классе Transport,
    # Он будет позволять расширят функционал других классов. Mixin в конце - обязательно
    @staticmethod
    def play_song_on_station(station) -> None:
        print(f"Play song on station {station}!")


class Car(Transport, RadioUserMixin):  # Также можно создать класс сигнализация, и добавить сюда
    pass


class Phone(RadioUserMixin):
    pass


car = Car("Kyev")
phone = Phone()

car.play_song_on_station("FM")  # Play song on station FM!
phone.play_song_on_station("Radio")  # Play song on station Radio!


class Clock(RadioUserMixin):
    pass

clock = Clock()
clock.play_song_on_station("FM")  # Play song on station FM!
