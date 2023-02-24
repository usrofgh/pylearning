#-----------------------------------------------------------------------------------------------------------------------
'Декоратор - функция принимающая ссылку на одну функцию, и возвращающая ссылку на другую функцию'
import sys


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs) #печатает имя ф-и и args с которыми она была вызвана
        return func(*args, **kwargs)
    return inner

@trace
def identify(x):
    'I do nothing useful.'
    return x

print(identify(42)) #identify (42,) {} 42

def identify_copy(x):
    'I do nithing useful.'
    return x

print(identify.__name__, identify.__doc__) # inner None - так как декоратор trace подменяет identity на inner
print(identify_copy.__name__, identify_copy.__doc__, '\n\n') # identify_copy / I do nithing useful.
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
'''чтобы возвращать корректные значения нужно присвоить их(ниже)'''
def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs) #печатает имя ф-и и args с которыми она была вызвана
        return func(*args, **kwargs)
    inner.__module__ = func.__module__
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

@trace
def identify(x):
    'I do nothing useful.'
    return x
print(identify(42))#identify (42,) {} / 42
print(identify.__name__, identify.__doc__, '\n\n') # identify I do nothing useful. - OK
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
'''как не вписовать __х__ а автоматически заменить?(ниже)'''
import functools
def trace(func):
    @functools.wraps(func) # ЛИБО ниже
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs) #печатает имя ф-и и args с которыми она была вызвана
        return func(*args, **kwargs)
    #functools.update_wrapper(inner, func)
    return inner

@trace
def identify(x):
    'I do nothing useful.'
    return x

print(identify.__name__, identify.__doc__, '\n\n') # identify I do nothing useful. - OK
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
trace_enabled =  False # global var с её помощью будем отключать и вкл trace. если выкл - возвращаем func

def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner if trace_enabled else func

@trace
def identify(x):
    'I do nothing useful.'
    return x
print(identify(42))
print(identify.__name__, identify.__doc__, '\n\n')
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
trace_enabled = False  # global var с её помощью будем отключать и вкл trace. если выкл - возвращаем func


def trace(handle):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs, file=handle)
            return func(*args, **kwargs)
        return inner
    return decorator


@trace(sys.stderr)
def identify(x):
    'test'
    return x

#print(identify(42)) #42

#Чтобы не делать такую вложенность - создай дек-р для деко-ров(ниже)
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
#декораторы с аргументами

def with_arguments(deco):
    @functools.wraps(deco)
    def wrapper(*dargs, **dkwargs):
        def decorator(func):
            result = deco(func, *dargs, **dkwargs)
            functools.update_wrapper(result, func)
            return result
        return decorator
    return wrapper

@with_arguments
def trace(func, handle):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs, file=handle)
        return func(*args, **kwargs)
    return inner

@trace(sys.stdout)
def identify(x):
    'testick'
    return x

print(identify(42)) #identify (42,) {} / 42
print(identify.__name__, identify.__doc__, '\n\n') #identify testick
#оказывается, так больше не пишут(как выше). Автор просто забил и перешел к упрощенной версии :D
#-----------------------------------------------------------------------------------------------------------------------










#-----------------------------------------------------------------------------------------------------------------------
#декораторы с опциональными аргументами - магическая версия

def trace(func=None, *, handle=sys.stdout): #указываем что handle нужно передавать только с именем чтобы не перепутать
    if func is None:
        return lambda func: trace(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner

@trace # тут аргумент func != None , так как ниже функция
def identify(x):
    'testick'
    return x

print(identify(42)) # identify (42,) {} / 42
print(identify.__name__, identify.__doc__) # identify testick