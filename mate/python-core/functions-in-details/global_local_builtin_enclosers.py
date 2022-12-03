# callback - функция к-ю мы передаем в другую ф-ю
# global, local, builtin, enclosing
# Не рекомендуется часто юзать global и одинаково называть global/local переменные
# python по умолчанию запрещает изменять глобальные переменные в local scope:
def printe():
    pass
	# s += "How are you?"   # дописать global для точного указания что нужна global переменная, иначе будет ошибка


# immedeately invoke lambda function  // не рек. юзать
(lambda x, y: x * y)(10, 5)

# It is good to use them when you have to implement a few methods but their number is not enough to create a class,
# so closure will provide a more readable solution.
# But when the number of attributes and methods gets larger, it's better to implement a class.

def fff(msg):
    def b():
        print(msg)
    return b


c = fff('Hello')  # тут a() уже заканчивет свое выполнение и замыкается для функции b(), чтобы сохранить для неё значение msg
c()  # Hello


def produce(device_name: str):
    count = 0
    b = 1
    def device():
        nonlocal count
        b = 2
        # count, не глобальная, но для ф-ии device и не локальная, поэтому юзаем nonlocal.
        # Без nonlocal можем только читать, но не перезаписывать
        count += 1
        print(f"{device_name} launch {count}")

    return device


cell_phone = produce('Cell Phone')
cell_phone()  # Cell Phone launch 1
cell_phone()  # Cell Phone launch 2
cell_phone()  # Cell Phone launch 3
cell_phone()  # Cell Phone launch 4

print(produce.__closure__)  # None

# (<cell at 0x0000027FCA04BEE0: int object at 0x00007FFBFC49D388>,
# <cell at 0x0000027FCA04BE80: str object at 0x0000027FCA036B70>)
# Это п-е к-е хранятся для inner-функции
print(cell_phone.__closure__)

print(cell_phone.__closure__[0].cell_contents)  # 4
print(cell_phone.__closure__[1].cell_contents)  # Cell Phone
