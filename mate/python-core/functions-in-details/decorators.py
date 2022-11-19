# ----------------------------------------- Декораторы
# https://youtu.be/D3gr2VAqXQ4?t=134
# для избежания дублирования кода конечно можно юзать мета функции, передавая туда переменную юзера и какую функцию
# выполнять, но можно просто юзать декоратор
# Декоратор - ф-я оборачивающая другую ф-ю и изменяет её поведение

def timer(func):
    def inner():
        import time
        s = time.time()
        r = func()
        e = time.time()
        print(f"Time taken: {e - s}")
        return r
    return inner

@timer
def long_function():
    return sum(range(50_000_000))

# decorated_long_f = timer(long_function)
# print(decorated_long_f())

print(f"Res: {long_function()}")

#-------------start----------------
# чтобы не писать эти 2 строки ,просто напиши над ф-ей "long_function" -
# @timer(синтаксический сахар), и дальше можно просто писать decorated_long_f()
# decorated_long_f = timer(long_function)
# print(decorated_long_f())
#-------------end------------------


# timer принимает ссылку на ф-ю которая будет "изменена", возвращает ссылку на "измененную функцию".
# По факту изменений поведения самой функции нет, просто возвращаем ссылку на ф-ю которая помимо исполнения
# переданной ф-и будет также делать другие вещи



#декоратор с аргументами

def timer(func):
    def inner(*args, **kwargs):
        import time
        s = time.time()
        r = func(*args, **kwargs)
        e = time.time()
        print(f"Time taken: {e - s}")
        return r
    return inner

@timer
def very_long_function(num_of_iterations):
    return sum(range(num_of_iterations))

# wrapped_f = timer(very_long_function)
# print(wrapped_f(num_of_iterations=1000))

print(very_long_function(num_of_iterations=10_000_000))

# декторатор, сложнее

def delay(seconds: int):
    def inner(func):
        def wrapper(*args, **kwargs):
            import time
            print(f"Sleeping {seconds} sec")
            for i in range(seconds):
                time.sleep(1)
                print(i + 1)
            func(*args, **kwargs)
        return wrapper
    return inner

@delay(seconds=3)
def hello(name: str):
    print(f"Hello {name}")
# delay(3)(hello)('Nikita') # не пиши та. Добавляей seconds как аргумент
hello('Nikita')

print(hello.__name__)  # Если не ф-я не обернута, будет hello, обернута декоратором - wrapper.
# help(hello) работает также, docstring будет выводиться от wrapper.
# Чтобы избежать, юзай декоратор над заменяющей ф-ей(wrapper) - functools.wraps(func)




#просто для теста
def deco1(func):
    def inner(*args, **kwargs):
        print("start1")
        func(*args, **kwargs)
        print("end1")
    return inner

def deco2(func):
    def inner(*args, **kwargs):
        print("start2")
        func(*args, **kwargs)
        print("end2")
    return inner

def deco3(func):
    def inner(*args, **kwargs):
        print("start3")
        func(*args, **kwargs)
        print("end3")
    return inner

@deco1
@deco2
@deco3
def say(message):
    print(message)

say("Hello world!")