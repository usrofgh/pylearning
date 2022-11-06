import functools
import time


def timethis(func=None, *, n_iter=100):
    if func is None:
        return lambda func: timethis(func, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, end=' ... ')
        acc = float('inf')
        for i in range(n_iter):
            tick = time.perf_counter()
            result = func(*args, **kwargs)
            acc = min(acc, time.perf_counter() - tick)
        print(acc)
        return result
    return inner

result = timethis(sum)(range( 10 ** 5))
print(result, '\n\n')
#-----------------------------------------------------------------------------------------------------------------------









#-----------------------------------------------------------------------------------------------------------------------
import functools

#считает к-во раз вызова inner в момент компиляции
def profiled(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.ncalls += 1 # атрибут ф-ции inner
        return func(*args, **kwargs)

    inner.ncalls = 0
    return inner


@profiled
def identify(x):
    return x

print(identify(42)) #42
print(identify.ncalls, '\n\n') #1
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        #inner.called = True
        if not inner.called:
            res = func(*args, **kwargs)
            inner.called = True
            return res
    inner.called = False
    return inner

@once
def initialize_settings():
    return 'Settings initialized.'


print(initialize_settings()) # Settings initialized.
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
#запоминает р-т  вычисления ф-й по её аргументу
def memoized(func):
    cache = {} #удобно юзать словарь для универсальной мемонизации
    #Кэш будет у каждой из функции свой. Тело вызывается для каждой йдекорируемой функции

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args, kwargs
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner

@memoized
def s(a, b):
    return a + b

print(s(1,2))