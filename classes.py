

class Counter:
    """I count. That is all."""

    """конструктор - инициализирует объект. В классах у методов всегда есть хотя бы
        один аргумент - self(экземляр класса). Можно назвать НЕ self, но тогда  
        коллеги поколечат
        
        Без self будет ошибка"""
    def __init__(self, initial=0):
        self.value = initial

    def increment(self):
        self.value += 1

    def get(self):
        return self.value


c = Counter(42)
c.increment()
c.get()  # 43

"""
В отличии от магического java/c++ у python нет 'this', вместо этого явно указывается self

Как и в других ООП языках python разделяет атрибуты экземплятра и атрибуты класса. Атрибуты экземпляра добавляются
присваиванием self - self.attribute = value
Аттрибуты класса объявляются в теле класса или прямым присваиванием к классу:
"""


class Counter:
    all_counters = []

    def __init__(self, initial=0):
        Counter.all_counters.append(self)  # объявляем атрибут класса в теле класса


Counter.some_other_attribute = 42
print(Counter.all_counters)

'''в python нет спец. указаний внешних/внутренних атрибутов как в java например. Для этого используют _ в начале
при назначении переменной'''

class Noop:
    some_attribute = 42
    # особые любители контроля используют 2 __, тогда коллегам усложится доступ к этим переменным. Рек юзать одно _
    _internal_atrribute = [2]
    __deep_internal_attribute = [1]


print(Noop._internal_atrribute)  # [2]
print(Noop._Noop__deep_internal_attribute)  # [1]
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
from collectionZ import deque


class MemorizingDict(dict):  # класс к-й сохраняет 10 последних ключей (история)
    _history = deque(maxlen=10)

    def set(self, key, value):
        self._history.append(key)
        self[key] = value

    def get_history(self):
        return self._history


d = MemorizingDict({'foo': 42})
d.set('baz', 100500)
print(d.get_history())  # deque(['baz'], maxlen=10)

d.set('boo', 500100)
print(d.get_history())  # deque(['baz', 'boo'], maxlen=10)
print(d['baz'])  # 100500
#-----------------------------------------------------------------------------------------------------------------------









#-----------------------------------------------------------------------------------------------------------------------
# abz внутренние атрибуты классов и экземпляров



class Noop:
    """I do nothing at all."""

print(Noop.__doc__)  # I do nothing at all.
print(Noop.__name__)  # Noop
print(Noop.__module__)  # __main__ - имя модуля в к-м класс объявлен. В данном случае модуля нет, поэтому main
print(Noop.__bases__)  # (<class 'object'>,) - базовые классы. Все неявно наследуются от Object
noop = Noop()
print(noop.__class__)  # <class '__main__.Noop'>
print(noop.__dict__)  # {} - это экземпляр класса
#  print(Noop.__dict__) - {} - это сам класс (тут много чего выведет)
print(Noop.__class__)  # <class 'type'>


# подробнее о dict

# добавление/изменение и удаление атрибутов - фактически операции со словарем.
# поиск атрибутов происходит динамически, мы заходим в словарь __dict__ и ищем атрибут
noop.some_attribute = 42
noop.__dict__['some_other_attributes'] = 100500
print(noop.__dict__)  # {'some_attribute': 42, 'some_other_attributes': 100500}
del noop.some_other_attributes  # {'some_attribute': 42}
vars(noop)  # {'some_attribute': 42} - фунция для печати атрибутов, лучше использовать вместо __dict__
#-----------------------------------------------------------------------------------------------------------------------







#-----------------------------------------------------------------------------------------------------------------------
# __slots__



# у экземпляров с __slots__ отсутствует __dict__, они занимаются меньше памяти
class Noop:
    __slots__ = ['some_attribute']  # других атрибутов у Noop не будет. Тут указываем какие будут

noop = Noop()
#  vars(noop)  TypeError: vars() argument must have __dict__ attribute
noop.some_attribute = 42  # 42
#  noop.some_other_attribute = 100500 - AttributeError: 'Noop' object has no attribute 'some_other_attribute'

# если делаю всё правильно - слот не нужен, нужен nametuple. Если знаю структуру - нет повода НЕ юзать nametuple
# nametuple сам использует __slots__
#-----------------------------------------------------------------------------------------------------------------------











#-----------------------------------------------------------------------------------------------------------------------
# abz связанные и несвязанные методы

class SomeClass:
    def do_something(self):
        print('Doing something.')


print(SomeClass().do_something)  # создается экз класса(не инициализируется. В print выводит ссылка на ф-ю экз класса
print(SomeClass().do_something())  # Doing something. - исполняется ф-я экз класса

print(SomeClass.do_something)  # просто ссылка на ф-ю, экз класса не фигурирует, нужно передавать явно


instanse = SomeClass()
SomeClass.do_something(instanse)  # Doing something - несвязанный метод. Явно передаем экземпляр 1-м аргументом









#-----------------------------------------------------------------------------------------------------------------------
# abz свойства
from os.path import dirname

class Path:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "Path({})".format(self.current)

    @property  # в __dict__ ключа parent не будет, тк. это свойство а не атрибут
    def parent(self):
        return Path(dirname(self.current))


p = Path('./decorators/test.txt')
# p.parent = 1 #  AttributeError: can't set attribute
print(p.parent)  # Path(./decorators)



# своства, изменение и удаление



class BigDataModel:
    def __init__(self):
        self._params = []  # params - свойство

    @property
    def params(self):  # метод должен называться как свойство
        return self._params

    @params.setter
    def params(self, new_params):  # метод должен называться как свойство
        assert all(map(lambda p: p > 0, new_params))
        self._params = new_params

    @params.deleter
    def params(self):  # метод должен называться как свойство
        del self._params


model = BigDataModel()
# вызываем функцию params инициализируя значениями. (@setter), и  выводим значения (@property). Визуально - одинаково
model.params = [0.1, 0.5, 0.4]
print(model.params)  # [0.1, 0.5, 0.4]
del model.params  # если params.deleter нет, будет ошибка - AttributeError: can't delete attribute
# print(model.params)  # AttributeError: 'BigDataModel' object has no attribute '_params'

# самое частое всё же использование getter'ов которые мы не хотим засовывать в __dict__, но хотим высунуть  как атрибут









#-----------------------------------------------------------------------------------------------------------------------
# abz наследование



class Counter:
    def __init__(self, initial=0):
        self.value = initial


class OtherCounter(Counter):
    def get(self):
        return self.value


c = OtherCounter()
print('get' in vars(c))  # False
print('get' in vars(OtherCounter))  # True

print(c.get())  # 0
print(c.value)  # 0
''' поиск имени при обращении к атрибуту или методу сначала ведется в __dict__ экземпляра.
Если там нет - в __dict__ класса, а затем рекурсивно по всех иерархии наследования
Если явно нигде не указан __init__, то будет идти по ирархии вверх пока не дойдет до класса к-й реализует'''



# abz super



class Counter:
    all_counters = []

    def __init__(self, initial=0):
        self.__class__.all_counters.append(self)
        self.value = initial


class OtherCounter(Counter):
    def __init__(self, initial=0):
        self.initial = initial
        super().__init__(initial)  # вызывает родительский конструктор


c = Counter()
print(c.value)  # 1

oc = OtherCounter()
print(vars(oc))  # {'initial': 0, 'value': 0}. было только свойство initial, но вывелось и value(родитель)
#-----------------------------------------------------------------------------------------------------------------------









#-----------------------------------------------------------------------------------------------------------------------
#abz предикат isinstance - проверяет что объект эклемпляр класса
# НЕ используй type при таких проверках
class A: pass
class B(A): pass
class C: pass
print(isinstance(B(), A))  # True
print(isinstance(B(), C))  # False
print(isinstance(B(), (A, B)))  # True - кортеж. Если хоть один true - вернет True
print(isinstance(B(), A) or isinstance(B(), C))  # True

# issubclass - проверяет что A наследник B класса - поэтому не пишем B() как в isinstance
print(issubclass(B, A))  # True
# print(issubclass(B, A, C))  # True
#-----------------------------------------------------------------------------------------------------------------------
# abz множественное наследование


class A:
    def f(self):
        print('A.f')


class B:
    def f(self):
        print('B.f')


class C(A, B):
    pass


C().f() # A.f
print(C.mro())  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# показывает в каком порядке разрешается метод. Сначала смотрим в С, потом в А, В и потом в object
