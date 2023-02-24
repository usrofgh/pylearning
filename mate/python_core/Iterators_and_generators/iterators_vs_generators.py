# В чем их отличие?
# Итератор - более глобальное понятие. Каждый генератор является под собою итератором
# Генератор сам выбросит StopIteration, поэтому не реализуем его
# Итератор хранит всё в экземпляре класса, джен - храни как локальную переменную

# В итераторе сначала нужно создать экз.класса с переданными итерируемыми значениями и обвернуть это функцией iter(),
# дальше можно юзать next().
# В генераторе нужно просто передать итерируемые значения в функцию, и юзать next
# В итераторе, чтобы пройтись по новой по списку, нужно просто для экз. класса
#   вызвать iter(обнуляет self.current_element). Для джен - по новой вызвать функцию


students = ["Alice", "Bob", "Karl", "John", "Kate"]


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


for elem in EachSecondElement(students):
    print(elem)  # Bob John


# -----------------------------------------------------------------------------------
def each_second_element(elements):
    current_element = 1
    while current_element < len(elements):
        yield elements[current_element]
        current_element += 2


for elem in each_second_element(students):
    print(elem)  # Bob John