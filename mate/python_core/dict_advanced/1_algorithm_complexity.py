# Сложность алгоритма - функция зависимости к-ва операций в алгоритме от n либо размера входных данных

# f(n) = C - к-во операций не зависит от размера входных данных(n). Ф-я имеет константное время выполнения
# f(n) = a*n + b - к-во операций пропорционально к-ву входных данных - линейная ф-я.  a,b - константы
# f(n) = a*n^2 + b*n + c - Если коэффициент а перед к-вом входных данных в квадрате не 0 то - квадратическая ф-я

# В вычислении алгоритмической сложности const не имеют большого значения

# O(N) - big "O" notation -
# O(1) - const time execution
# O(N) - linear time execution
# O(N^2) - квадратическая сложность
# O(Log n) - на каждом шаге откидываем половину значений, например бинарный поиск
# https://prnt.sc/wlM1HbOaKX5P


# Big Omega: represents the lower bound.
# Big Theta: represents both the lower and upper bounds.

# Big O: represents the upper bound. it’s the most relevant for performance analysis,
# as it helps us to understand the worst case behaviour



from time import perf_counter

# 2 * O(1) = O(1) - const function
def add(a: int, b: int):
    sum_ = a + b  # const operation # O(1)
    print(sum_)  # O(1)
    return sum_


# O(N) - linear
def print_list(ls: list):
    for el in ls:
        print(el)  # O(1)


numbers = [1, 2, 3, 4]

# O(n^2) - квадратическая сложность
def print_matrix(matrix: list[list[int]]):
    n = len(matrix)
    for i in range(n):  # O(n)
        for j in range(n): # O(n)
            print(matrix[i][j])


def find_position(ls: list, to_find: int):
    for index, element in enumerate(ls):
        if element == to_find:
            return index

    return -1

find_position([1, 2, 3, 4, 5], 1)  # 1 // O(1) - лучший случай
find_position([1, 2, 3, 4, 5], 6)  # -1 // 0(n) - худший случай
find_position([1, 2, 3, 4, 5], 3)  # 0(n) / 2 - среднее выполнение. По сколько const не особо интересны - O(n)