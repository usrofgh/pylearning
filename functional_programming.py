"""
ограничена, может принимать аргументы и возвращать операции с ними
for быть там не может
lambda arguments: expression
полезная с ф-ми к-е принимают другие ф-и, например map
вызывать ф-ю для к-го элемента map
"""

# map не рек юзать, map идет с js вроде
# map устарелая вещь, был добавлен раньше чем list compr, лучше юзать его. в целом по скорости одинаковые


print(*map(lambda x: x * 7, range(7)))  # 0 7 14 21 28 35 42
"top - * - без {}"
print(list(map(lambda s: s.strip(), open('./1.txt'))))
print(set(map(lambda s: s.strip(), open('./1.txt'))))
"top - с {} "

print(list(map(lambda x, n: x ** n, [2, 3], range(1, 8))))
"""range укоротился т.к ориентируется на меньшую длинну - 2,3"""




#abz
'''filter - убирает из последовательности э-ты, не удовлетворяю
щие предикату'''

print(*filter(lambda x: x % 2 != 0, range(10))) #1,3,5,7,9

xs = [0, None, [], {}, set(), "", 42]
print(*filter(None, xs)) #42 - все что true - оставим, другое - нет


'''zip'''
print(*zip('abc', range(3), [42j, 42j, 42j])) #('a', 0, 42j) ('b', 1, 42j) ('c', 2, 42j)
print(*zip('abc', range(10))) #('a', 0) ('b', 1) ('c', 2)

#abz
'''генераторы списков'''
g = [x ** 2 for x in range(10) if x % 2 == 1]
#print(g) #[1, 9, 25, 49, 81]


'''генератор с вложенными списками'''
nested = [range(5), range(8, 10)]
g = [x for xs in nested for x in xs]
#лучше юзать обычный for так не очень понятно

#print(g) #[0, 1, 2, 3, 4, 8, 9]