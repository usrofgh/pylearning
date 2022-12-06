def find(element, arr):
    for i in range(len(arr)):  # инкремент итератора зависит от к-во э-в в массиве. i обозначим в формуле как n
        if i == element:
            return i
    return None

data = list(range(10+1))

print(find(4, data))
print(find(11, data))
print(find(1, data))

# 4 - как я понимаю input значение
# n - к-во э-в(итератор)
# 2 - к-во константных операций в функции - создание итератора, его инкремент i+=1. Не 3, так как не факт что будет
# возврат i

# 4n + 2 - алгоритм имеет линейную сложность. Можно записать как:
# O(n). Где 4,2, почему учитываем только n? - Так как независимо от к-ва входных э-в, числа 4 и 2 всегда константы
# поэтому не учитываем их

#----------------------------------------------------------------------------------------------------------------------


def combine(el):
    res = []  # 1
    for i in range(len(el)):  # 1, 1
        for j in range(len(el)):  #
            res.append(el[i] + el[j])
    return res  # 1


# res, i, j, i_iter, j_iter^2,  len(el)x2, el sum, append, res - 9 static actions
print(combine(['a', 'b', 'c']))
print(combine(['a', 'b', 'c', 'd']))

