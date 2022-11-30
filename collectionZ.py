# abz встроенные коллекции
t = ('a')  # str. Считывает просто как str с приоритетностью операции
t = ('a', )  # tuple
t = tuple(), (0, ) * 3   # ((), (0, 0, 0)) - коллекция из пустой коллекции и коллекции из 3-х элементов
l = list(), [0] * 3  # ([], [0, 0, 0]) - lists in tuple
s = set()
d = {}

# abz кортеж - используется для представления разнородных данных

date = 'October', 5  # () лучше всегда опускать если э-в > 1
xs = (42, )  # с 1-м э-м со (). Без () будет int
#-----------------------------------------------------------------------------------------------------------------------









#-----------------------------------------------------------------------------------------------------------------------
# abz кортеж и слайсы

person = ('George', 'Clain', 'May', 12, 1937)
name, birthday = person[:2], person[2:]  # ('George', 'Clain') ('May', 12, 1937) -      именованные слайсы
# чтобы избежать магических констант выше - можем дать имена слайсам
NAME, BIRTHDAY = slice(2), slice(2, None)
print(person[NAME], person[BIRTHDAY])  # ('George', 'Clain') ('May', 12, 1937) - вариант не плохой, но можно лучше
print(type(NAME), type(BIRTHDAY))  # <class 'slice'> <class 'slice'>

t = tuple(reversed((1, 2, 3)))
print(t)  # (3, 2, 1)
print(t[::-1])  # (1, 2, 3)
# зачем reversed если есть [::-1] - экономит память

for i in range(10+1): # range до 10 включая. Лучше так писать чем range(11)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9 10
print('\n')


x, y = (1, 2), (3, )
print(id(x), id(y))  # 2038041794112 2038040797392 / id - адрес объекта в памяти // x is y (сравнивается ячейка памяти)
print(x + y)  # (1, 2, 3) - р-т конкатенации - новый кортеж

# сравнение
cmpr1 = (1, 2, 3) < (1, 2, 4)
cmpr2 = (1, 2, 3, 4) < (2, )
cmpr3 = (1, 2, 3) < (1, 2, 3, 1)
print(cmpr1, cmpr2, cmpr3)  # True True True
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
# abz tuple
dataset = ('Ivan', 'Nikita', 'Oleg', 'May', 'October', 'August', 15, 31, 28, 1951, 1972, 1921)
NAME = slice(3)
MONTH = slice(3, 6)
DAY = slice(6, 9)
YEAR = slice(9, None)
print(dataset[YEAR])

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])  # создаем класс-кортеж Person с полями name, age.
# Каждый э-т будет с 2-мя полями. nametuple - фабрика классов
# ВСЕГДА когда нужно использовать кортеж, нужно использовать ИМЕННОВАНЫЙ кортеж - иначе не нужне кортеж
# Если не можете назвать поля - не нужен кортеж, если можете - namedtuple

p = Person('George', age=77)  # создаем экземпляр класса
print(p._fields)  # ('name', 'age')
print(p.name)  # George
print(p.age)  # 77
print(p._asdict())  # {'name': 'George', 'age': 77} - превращаем в dict
p = p._replace(name='Bill')  # меняем имя в новом созданном кортедже  Старый кортедж не изменяется
print(p.name)  # Bill.
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
# abz список списки list
l = [0] * 3
l1 = ["", ] * 5
print(l, l1)  # [0, 0, 0] ['', '', '', '', '']

print([1, 2, 3].copy())  # копирует
print([1, 2, 3][:])  # копирует

chunks = [[0]] * 2  # [[0], [0]]
chunks[1][0] = 1  # [[1], [1]]
# в чем разница?
# При первом варианте копируется ссыла на объект, а не создаются 2 разных объекта []
chunks = [[0], [0]]  # [[0], [0]]
chunks[1][0] = 1  # [[0], [1]]

# правильный способ:
chunks = [[0] for i in range(1 + 1)]
chunks[1][0] = 1  # [[0], [1]]

xs = [1, 2, 3]
xs.append(42)  # [1, 2, 3, 42]
xs.append({-1, -2})  # [1, 2, 3, 42, {-1, -2}]
xs.extend({-1, -2})  # [1, 2, 3, 42, {-1, -2}, -1, -2] EQUAl xs += {-1, -2}

xs = [1, 2, 3]
xs.insert(0, 4)  # [4, 1, 2, 3]
xs.insert(-1, 12)  # [4, 1, 2, 12, 3]

xs = [1, 2, 3]
xs[:2] = [0] * 2  # [0, 0, 3]
xs[:] = [1]  # [1] - заменяем всё содержимое

xs = [1, 2, 3]
xs += [4, 5]  # [1, 2, 3, 4, 5] ~~ xs = xs.extend([])

"""def f():
    xs += [42]
f()
Ошибка, так как пытаемся прибавить к несуществующей переменной xs, ибо инициализируем не по ссылке.
Если сделать xs.append(42) - все будет ок 
"""
xs = []
xs += 'abc'  # ['a', 'b', 'c']


# удаления э-тов

xs = [1, 2, 3, 4, 5, 6]
del xs[:2]  # [3, 4, 5, 6]. del ничего не возвращает
del xs[1]  # [3, 5, 6]
del xs[:]  # []

xs = [1, 2, 3]
a = xs.pop(1)  # удаляет э-т по индексу и возвращает значение удаленного э-та
print(a)  # 2

xs = [1, 2, 1, 0]
xs.remove(1)  # [2, 1, 0] - удаляет 1-е вхождение в списке
# xs.remove(5)  # ValueError: list.remove(x): x not in list

xs = [1, 2, 3]
xs.reverse()  # [3, 2, 1] - переворачивает список - ничего не возвращает
print(list(reversed(xs)))  # [1, 2, 3] - возвращает перевернутый список



xs = [3, 2, 1]
sorted(xs)  # [1, 2, 3] возвращает новый отсортированный список.
print(sorted({'a': 1, 'b': 2, 'd': 4}))  # Сортирует разные коллекции # sort() сортирует только list()
xs = [1, 2, 3]



################################################################################
strings = ["good", "bad", "excellent", 'good', 'bad', 'good']


def marks_order(mark:str):
    if mark == 'bad':
        return 1
    if mark == 'good':
        return 2
    return 3


print(sorted(strings))  # ['bad', 'bad', 'excellent', 'good', 'good', 'good'] - по алфавиту
print(sorted(strings, key=marks_order))  # ['bad', 'bad', 'good', 'good', 'good', 'excellent']
################################################################################





################################################################################
xs = [3, 2, 1]
xs.sort()  # [1, 2, 3] - сортирует список, ничего не возвращает

xs.sort(key=lambda x: x % 2, reverse=True)  # [1, 3, 2] / reverse=True - по убыванию.
xs.sort(key=lambda x: x % 2, reverse=False)  # [2, 1, 3]

xs = [(1, 2), (-3, 4)]
xs.sort(reverse=True)
print(xs)

#cmp_to_key
#-----------------------------------------------------------------------------------------------------------------------









#-----------------------------------------------------------------------------------------------------------------------
# abz deque
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # 2
print(stack)  # [1]

# Список - очередь, очередь
q = []
q.append(1)
q.append(2)
print(q.pop(0))  # 1 - с помощью pop(0) достаем из начала. Так не пиши - пиши как ниже
print(q)  # [2]


'''добавление/удаление из списка происходит за константное время,индексирование -за время,линейное от размера очереди'''
from collectionZ import deque
q = deque([1, 2, 3])
q.appendleft(0)  # deque([0, 1, 2, 3])
q.append(4)  # deque([0, 1, 2, 3, 4])
q.popleft()  # deque([1, 2, 3, 4])
q.pop()  # deque([1, 2, 3])
print(q[0])  # 1

q = deque([1, 2], maxlen=2)
q.appendleft(0)  # deque([0, 1], maxlen=2)
q.appendleft(1)  # deque([1, 0], maxlen=2)
q.append(2)      # deque([0, 2], maxlen=2)
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
# abz множества set  union

xs, ys, zs = {1, 2, 3}, {2, 3}, {3, 4}
un = set.union(xs, ys, zs)  # {1, 2, 3, 4}

un = set.intersection(xs, ys, zs)  # {3}
print(un)
un = set.difference(xs, ys, zs)
print(un)  # {1} - в xs есть то, чего нет в остальных
print(xs.isdisjoint(ys))  # True - if no one element exists in another set. False if one element exists in another set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
print(x.isdisjoint(y))  # true


seen = set()
seen.add(42)  # {42}
seen.update([1, 2])  # {1, 2, 42}
seen.update([], [1], [2], [3])  # {1, 2, 42, 3}


seen = {1, 2, 3}
seen.remove(3)  # {1, 2}
#seen.remove(5)  # KeyError: 5
seen.discard(5)  # ошибки нет. Удаляет только если э-т есть
seen.clear()  # set()


'''Множество в python это хеш-сет, то есть он может содержать только э-ты, к-е можно захешировать, то есть те,
которые неизменяемые'''
# a = {set(), set()}  # error
seen = {frozenset(), frozenset()}  # {frozenset()} - содержит все операции set() кроме add/remove. Это замороженный set










#-----------------------------------------------------------------------------------------------------------------------
# abz словарь dict
# ключем может быть только НЕизменяемый тип данных
#d = {foo='bar'} - error
d = dict(foo='bar')  # {'foo':'bar'}
d = dict(d, boo='faz')  # {'foo': 'bar', 'boo': 'faz'}
d = dict.fromkeys(['foo', 'bar'])  # {'foo': None, 'bar': None}
d = dict.fromkeys('abc', 0)  # {'a': 0, 'b': 0, 'c': 0}


# Если инициализатор изменяемое значение, то значит он не нужен, ибо ведет себя не так как ожидается (??? - вроде понял)
d = dict.fromkeys('abcd', [])  # {'a': [], 'b': [], 'c': [], 'd': []}
d = {ch: [] for ch in 'abcd'}  # {'a': [], 'b': [], 'c': [], 'd': []}

d = dict.fromkeys(['foo', 'bar'], 42)  # {'foo': 42, 'bar': 42}
d.keys()  # dict_keys(['foo', 'bar'])
d.values()  # dict_values([42, 42])
d.items()  # dict_items([('foo', 42), ('bar', 42)])
len(d.items())  # 2
print(42 in d.values())  # True
print({v for v in d.values()})  # True

'''for k in d:
    del d[k]'''  # error RuntimeError: dictionary changed size during iteration

# Чтобы не было ошибки - нужно сделать копию

'''for k in set(d):
    del d[k]'''

d = dict(foo='bar')
print(d['foo'])  # bar
# d['arj']  # KeyError: 'arj'

# Проверить наличие ключа
print('arj' in d)  # False
print('foo' in d)  # True
d.get('arj', 42)  # 42
d.get('arj')  # None // by default

d = dict(foo='bar')
d.setdefault('biz', '???')  # если значения нет - добавляет, если есть - возвращает
print(d)  # {'foo': 'bar', 'biz': '???'}

d.update([('foo1', 'bar')], boo=42)  # {'foo': 'bar', 'biz': '???', 'foo1': 'bar', 'boo': 42}
del d['boo']
a = d.pop('foo1')  # bar / возвращает значение для ключа который я удалил
d.clear()

#  происходит перезапись
data = {'3': 1, "3": 2, 3:3, 1 + 2: 4, 3.0 : 5}
print(data)  # {'3': 2, 3: 5}
data = {1: 1, True: 2}  # True == 1
print(data)  # {1: 2}

#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
# abz collections defaultdict

g = {'a': {'b'}, 'b': {'c'}}
print(g['a'])  # {'b'}
# ['c'].add('a')  # ошибка, так как вершини 'c' нет в dict. Чтобы этого избежать, используй defaultdict

from collectionZ import defaultdict
g = defaultdict(set, **{'a': {'b'}, 'b': {'c'}})  # при отсутствии э-та будет создан set со всеми необходимыми э-ми
# set без () так как мы передаем функцию к-ю нужно исполнить если э-т будет отсутствовать
g['c'].add('a')  # defaultdict(<class 'set'>, {'a': {'b'}, 'b': {'c'}, 'c': {'a'}})

# OrderedDict - в каком порядке добавляю э-ты в таком и итерирую
from collectionZ import OrderedDict
d = OrderedDict([('foo', 'bar'), ('boo', 42)])





# Counter - позволяет подсчитать в словаре к-во хешируемых объектов
from collectionZ import Counter
c = ['foo' for v in range(10)]
c = Counter(c)  # Counter({'foo': 10})
c['bar'] = 1
c['bar'] += 1  # Counter({'foo': 10, 'bar': 2})
# поддерживает все методы словаря, и реализует несколько дополнительных
print(c.pop('foo'))  # 10
print(c['bar'])  # 2
print(c['boo'])  # 0 - такого ключа нет. Вместо исключения возвращает 0

c = Counter(foo=4, biz=0, bar=-1)
print(*c.elements())  # foo foo foo foo / перчисляются только >0 элементы(только для elements() метода
print(list(c.elements()))  # тоже что и сверху, но без * а с list()
print(c.most_common(1))  # [('foo', 4)] / топ N самых частых э-в


print(c)  # {'foo': 4, 'biz': 0, 'bar': -1}
c.update(['bar'])  # {'foo': 4, 'biz': 0, 'bar': 0} поэлементно обновить значение bar на число по умолчанию - 0
c.subtract({'foo': 2})  # {'foo': 2, 'biz': 0, 'bar': 0} / поэлементно обновить foo на 2


c1 = Counter(foo=4, bar=-1)
c2 = Counter(foo=2, bar=2)
# все ключи с отрицательным значением выкидываются
r = c1 + c2  # Counter({'foo': 6, 'bar': 1})
r = c1 - c2  # Counter({'foo': 2})
r = c1 & c2  # Counter({'foo': 2})
r = c1 | c2  # Counter({'foo': 4, 'bar': 2})
# Р-т любой из бинарных операций всегда содержит только ключи с положительными частотами