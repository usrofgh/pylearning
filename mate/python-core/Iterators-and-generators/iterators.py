s = ['1', '2', '3', '4']

i = iter(s)
print(next(i))  # 1
print(next(i))  # 2
print(i.__next__())  # 3
print(next(i))  # 4
# print(next(i)) # StopIteration error

# Цикл юзает этот iter. но куда девается ошибка StopIteration?
# Работа цикла "for x in y: print(x)" под капот:ом:
iterator = iter(s)
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break


# Собственный итератор:
class EachSecondElement:
    def __init__(self, elements):
        self.elements = elements

    def __iter__(self):
        self.current_element = 1
        return self

    def __next__(self):
        if self.current_element >= len(self.elements):
            raise StopIteration

        result = self.elements[self.current_element]
        self.current_element += 2
        return result


# Тут ходим по кругу, raise удаляем, остаток добавляем
# def __next__(self):
#     result = self.elements[self.current_element]
#     self.current_element += 2
#     self.current_element %= len(self.elements)
#     return result


students = ["Alice", "Bob", "Carl", "John", "Kate"]
each_second_person = EachSecondElement(students)
i = iter(each_second_person)
print(next(i))  # Bob
print(next(i))  # John
# print(next(i)) # StopIterationError
print('\n')
for student in EachSecondElement(students):
    print(student)  # Bob John
