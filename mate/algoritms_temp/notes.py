# ---------- Algorithms and Data Structures / Data Structures: Array ----------
# ---------- Quick overview of arrays ----------


#  инициализировался массив размером 3
# в каждый из его индексов записались значения
lst = list(range(10_000_000))
print(id(lst))
# Для этого под капотом берутся ячейки памяти из старого массива, к ним выделяется больше памяти для значений
# из указанного другого массива и добавляются.
# Перед/После конкатенации в ту же переменную номер ячейки памяти не меняется
lst += [10, 11]
print(id(lst))


def benchmark(func) -> callable:
    import time

    def inner(*args, **kwargs):
        s = time.perf_counter()
        func(*args, **kwargs)
        e = time.perf_counter()
        print(f'{func.__name__} Elapsed: ', round(e - s, 2))

    return inner


n = 1


@benchmark
def lst_get(elements: list, index: int) -> None:
    elements[index]


@benchmark
def lst_insert(elements: list, index: int) -> None:
    elements.insert(index, 1)


@benchmark
def lst_pop(elements: list, index: int) -> None:
    elements.pop(index)


@benchmark
def lst_remove(elements: list, value: int) -> None:
    elements.remove(value)


lst = list(range(150_000_000))
lst_last_index = len(lst) - 1
lst_average_index = len(lst) // 2

# 150 000 000
lst_get(lst, 0)  # 0.0
lst_get(lst, lst_last_index)  # 0.0
lst_get(lst, lst_average_index)  # 0.0

lst_insert(lst, 0)  # 1.7
lst_insert(lst, lst_last_index)  # 0.0
lst_insert(lst, lst_average_index)  # 0.06

lst_pop(lst, 0)  # 0.09
lst_pop(lst, lst_last_index)  # 0.0
lst_pop(lst, lst_average_index)  # 0.05

lst_remove(lst, 0)  # 0.1
lst_remove(lst, 149_999_999)  # 5.85
lst_remove(lst, 100_000_000)  # 3.83

lst.append(1)  # 0.0
# ![](img.png)