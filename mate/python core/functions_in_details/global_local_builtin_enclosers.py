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

    def device():
        nonlocal count
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