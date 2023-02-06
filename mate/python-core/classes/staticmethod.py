# Используется когда НЕ нужен доступ ни к экземпляру, ни к классу
# в нем нельзя изменить атрибуты класса/объекта. Он просто принимает аргументы и работает с ними


class Car:
    def __init__(self, max_speed_km: int):
        self.max_speed_km = max_speed_km

    def print_max_speed_km(self):
        print(f"Car's maximum speed is {self.max_speed_km} km/h")

    def print_max_speed_miles(self):
        # не ясно что это за коэффициент, лучше создать отдельный метод, к-й будет конвертировать км в милли
        print(f"Car's maximum speed is {self.km_to_miles(self.max_speed_km)} miles/h")
        # print(f"Car's maximum speed is {self.km_to_miles(self.max_speed_km)} miles/h")

    # Тут не используется экземпляр класса, поэтому селф не нужен, добававь @staticmethod
    # def km_to_miles(self, km: int) -> float:
    #     return round(km * 0.62137119, 1)

    @staticmethod
    def km_to_miles(km: int) -> float:
        # 1 km =  0.62137119 miles
        return round(km * 0.62137119, 1)

    # Зачем @staticmethod если можно создать метод вне класса, и юзать без self? - не всегда удобно, иногда лучше чтобы
    # функция принадлежала классу


tesla_roadster = Car(max_speed_km=400)
tesla_roadster.print_max_speed_miles()