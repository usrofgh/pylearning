# В dict меньший шанс опечататься из-за группирования данных, нежели в переменной
# В классах можно группировать как свойства, Так и функции, которые принадлежат конкретным объектам
# можно добавлять свойства другим экземплярам класса
# Пример: С помощью чертежа дома можно построить несколько домой. Чертеж - класс, разные дома - объекты

# Не функция, а метод
# не переменная, а атрибут объекта
# self - ссылка на экземпляр класса, подставляется автоматически


class Person:
    pass



petia = Person()
petia.name = "Petia"
petia.last_name = "Smith"
petia.wife = None

tania = Person()
tania.name = "Tania"
tania.last_name = "Sevelina"
tania.husband = None

petia.wife = tania
print(petia.wife.name)  # Tania
print(tania.husband)  # None
tania.husband = petia
print(tania.husband.name)  # Petia

print(tania.last_name)  # Sevelina
petia.wife.last_name = petia.last_name
print(tania.last_name)  # Smith

petia.wife = Person()
petia.wife.last_name = petia.last_name  # тут мы 3-эму экземпляру присваиваем значение
print(petia.wife.__dict__)  # {'last_name': 'Smith'}
print(tania.last_name)  # Smith