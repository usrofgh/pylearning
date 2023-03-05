# CPython

# Reference counting - подсчет ссылок на ячейку памяти.
# Когда достигается 0, ячейка маркируется как мусорная
# Когда к-во мусорных объектов в памяти доходят до порогового GC очищает память.
# при запуске GC программа не выполняется

# Если объект пережил очистку, он переходит на следующее поколение, последнее поколение активно до завершения программы
# reference counting невозможно отключить
import gc
print(gc.get_threshold())  # (700, 10, 10) 1,2,3 поколения - порог
print(gc.get_count())  # (512, 5, 1) - к-во объектов в каждом поколении в моей программе
gc.collect(generation=0)  # вручную запускаю очистку
print(gc.get_count())  # (0, 6, 1). Указал бы gen=1. было бы (0, 0, 1)
gc.set_threshold(1000, 15, 15)  # ручная установка порогов
print(gc.get_threshold())  # (1000, 15, 15)


# GC не работает с циклическими ссылками(ссылкаются на себя же) a = [] a.append(a) - тут никогда a не достигнет нуля
# Решение - Generational Garbage Collection к-й прерывает это и удаляет такие объекты


from sys import getrefcount


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def __del__(self):
        print(self.name, "deleted")

cat = Animal("Cat1")
print(getrefcount(cat))  # 2  // в docs написано отнимать единицу. По факту тут 1
pet = cat
print(getrefcount(cat))  # 3
print(getrefcount(pet))  # 3
print(getrefcount(Animal("cat")))  # 1

print("\n\nGarbage collector")
# Garbage collector

cat = Animal("Cat1")
pet = cat
the_same_cat = cat
print(getrefcount(cat))  # 4
del the_same_cat
del pet
print(getrefcount(cat))  # 2
del cat  # Cat1 deleted // garbage collector runs if python deems it necessary. Сейчас эта полка маркировалась как мусор

cat = Animal("Cat1")
print(getrefcount(cat)) # 2
# Под конец также выведится Cat1 deleted, так как GC удалит все данные из памяти работы этой программы

print(getrefcount("I love Python!"))  # 3  // immutable starts from 3. mutable from 1
print(getrefcount([]))  # 1
a = []
print(getrefcount(a))  # 2
print(getrefcount(5435345345345))  # 3
print(getrefcount(0))  # 298
print(getrefcount(1))  # 196
