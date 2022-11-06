def wrapper():
    def identity(x):
        return x

    return identity


f = wrapper()
#print(f(42)) #42



def make_min(*, lo, hi):
    def inner(first, *args):
        res = hi
        for arg in (first, ) + args:
            if arg < res and lo < arg < hi:
                res = arg
        return max(res, lo)

    return inner

a = make_min(lo=0, hi=255)

#abz
#в питоне 4 обл. видимости
print(min)  # builtin. also  print etc.
min = 42  # global
def f(*args):
    min = 2
    def g(): #enclosing - все что выше local но не global
        min = 4 #local
        print(min)

f(1)
#LEGB
#например переменная в g функции. Если не нашли там(local)
# пойдем наверх - f(), если там нет - global, если там нет built

print(globals()) # {... 'min':42}

def f():
    min = 2
    max = 3
    print(locals())

f() # {'min': 2, 'max': 3}



def f():
    print(i)
for i in range(4):
    f() # 1,2,3 - поиск имени запускается после запуска ф-ции f()
    #в local i не найдено, переходим сразу в global, там есть i


min = 42
def f():
    min += 1
    return min
#f() - error. min + 1  пройдет, найдет из global, однако для присваивания
#с-ма будет искать min из local, а там её нет
#Если нужно указать что вы именно это и хотите присвоить, то:

min = 42
def f():
    global min
    min += 1
    return min
print(f())  #/43 - тут явно указываем что инкрементируем global min а не local



"""
указываем что хотим инициализировать НЕ local value, чтобы не создавалась
локальная копия в set а бралось из объемлиющей о-сти видимости
функции value и инициализировалось
global не используется в целом, используется nonlocal
"""
def cell(value=None):
    def get():
        return value
    def set(update):
        nonlocal value
        value = update
    return get, set

get, set = cell()
set(42)
print(get())
