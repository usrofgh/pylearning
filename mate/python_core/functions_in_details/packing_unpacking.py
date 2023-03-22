a, b, c = '123'  # a = 1, b = 2, c = 3
a, b, c = range(3)  # a = 0, b = 1, c = 2


d = {'one': 1, 'two': 2, 'three': 3}
a, b, c = d  # только ключи
a, b, c = d.items()  # и ключ и значение


a, b, c = {'a', 'b', 'c'}  # неупорядоченная инициализация


a = 1
b = 2
a, b = b, a  # swapping. меняем значения местами. Тут кортеж (b, a) я распаковываю в a, b


# a, b = 1, 2, 3   # error
*a, b = 1, 2, 3  # [1, 2], 3: a пытается захватить как можно значений, когда захвачивает "3",
# то понимает что не останется значений для b, поэтому "3" не захватывала и оставила для b
*a, b, c = 1, 2, 3  # [1], 2, 3
*a, b, c, d = 1, 2, 3  # [], 1, 2, 3


# *a = range(10)  # error
*a, = range(10)  # [0-9]


arr = ['meaningful', 'information', 'extra','extra', 'extra', 'extra',]
important, info, *_ = arr  # первые 2 переменные - meanigful, information, остальное сохраняется в "_"


t = 1, 2, 3
r = 0, *t, 4  # (0, 1, 2, 3, 4)


d = {'one': 1, 'two': 2}
r = {'four': 4, **d}  # {'four': 4, 'one': 1, 'two': 2}
merge = d | r  # {'one': 1, 'two': 2, 'four': 4}

def f(*котреж_для_значений):
    print(котреж_для_значений)  # (1, 2, 3)
f(1, 2, 3)


def f(**словарь_для_значений):
    print(словарь_для_значений)  # {'a': 1, 'b': 2, 'c': 3}
f(a=1, b=2, c=3)


def add(required: int, optional: int = 0, *args, **kwargs) -> int:
    print(required)
    print(optional)
    print(args)
    print(kwargs)
    print('\n')

add(1, 2, 3, 4, c=3, b=4)  # 1 2 (3, 4) {'c': 3, 'b': 4}
add(1, 'b', 'c', c=3, d=4)  # 1 b ('c',) {'c': 3, 'd': 4}  //  обрати внимание, что тут 'b' принимает optional(int), а не кортеж
add(1, c=3)  # 1 0 () {'c': 3}
add(1)  # 1 0 () {}
add([1, 2, 3, 4, 5])  # [1, 2, 3, 4, 5] 0 () {}
add(*[1, 2, 3, 4, 5])  # 1 2 (3, 4, 5) {}


first = {"one": 1, "two": 2, "three": 333}
second = {"three": 3, "four": 4}
united = {**first, **second}  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}


#так часто делают сторонние либы и фреймворки, поэтому *args не в конце
# нужно чтобы юзер всегда указывал именные аргументы для передачи, чтобы не передавали позицийно
def function(first, *args, second, **kwargs):
    pass