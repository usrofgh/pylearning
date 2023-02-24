# abz - list comprehension
# всегда создается новый список при list compr
a = [*range(100)]  # тут не написать условие и в list(range(100)) тоже
print(a)
a = [i for i in range(100) if '3' in str(i)]  # тут можно
print(a)

# ----------------------------------------------------------------------------------------------------------------------


# abz - Nested list comprehension
students_group = [["Anna", "John", "Liza", "Vlad"],
                  ["Mike", "April", "Bob", "Alice"],
                  ["Alex"]]

# for справа - первый, получает из листа группы, на выходе выдает группу
# for слева - второй, итерируется по студентам в группе, выдает конкатенируемое значение
a = [[student + " - Python" for student in group] for group in students_group]


# ----------------------------------------------------------------------------------------------------------------------


# abz dict comprehension
a = {i: i ** 2 for i in [4, 2, 7, 10] if i % 2 == 0 if i < 100000}  # {4: 16, 2: 4, 10: 100}

shadow = [["Monday", "Tuesday", "Wednesday", "Friday"], ["Tuesday", "Wednesday", "Tuesday", "Friday"]]
a = {i: sum(shadow, []).count(i) for i in set(sum(shadow, []))}


# ----------------------------------------------------------------------------------------------------------------------


# abz walrus operator
import random
print([temp for _ in range(20) if (temp := random.randrange(90, 110)) >= 100])
