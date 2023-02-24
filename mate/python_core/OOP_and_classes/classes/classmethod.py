# используется когда не нужен доступ к объекту, а нужен доступ к классу
class Citizen:
    city = "Springfield"

    def __init__(self, full_name: str):
        self.full_name = full_name

    def change_city_name(self, new_name: str):
        self.city = new_name


mayor = Citizen("Joe Quimby")
homer = Citizen("Homer Simpson")

mayor.change_city_name("Tokyo")
print(mayor.city)
print(homer.city)  # Springfield // по-прежнему остается. Так как выше создается новый аттрибут экз класса.
# Чтобы изменять в функции именно аттрибут класса, не нужно передавать self, для этого впиши classmethod над методом


class CitizenNew:
    city = "Springfield"

    def __init__(self, full_name: str):
        self.full_name = full_name

    @classmethod
    def change_city_name(cls, new_name: str):
        cls.city = new_name


mayor = CitizenNew("Joe Quimby")
homer = CitizenNew("Homer Simpson")

mayor.change_city_name("Tokyo")
print(mayor.city)  # Tokyo
print(homer.city)  # Tokyo