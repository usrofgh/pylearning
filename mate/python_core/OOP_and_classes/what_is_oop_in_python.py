# OOP_and_classes - стиль написания кода, где классы/объекты выходят на 1-й план
# Пытается описать сложные зависимости из реальной жизни в виде кода
# Парадигмы: Наследование, Инкапсуляция, Полиморфизм, Абстракция


# Разница в подходах:
# Class-based. Все привязано к классу/экз. класса
class Employee:
    bonus_coefficient = 1.1

    def __init__(self, base_salary: int) -> None:
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary * Employee.bonus_coefficient

# Function based. Всё независимо, ни к чему не привязано
bonus_coefficient = 1.1


def calculate_salary(base_salary: int) -> float:
    return base_salary * bonus_coefficient

john_oop = Employee(19_500)
print(john_oop.calculate_salary())  # 21450.0
print(calculate_salary(19_500))   # 21450.0
#-----------------------------------------------------------------------------------------------------------------------