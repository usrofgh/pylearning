CALCULATOR_VERSION = "1"


def add(a: int | float, b: int | float) -> int | float:
    return a + b


def multiply(a: int | float, b: int | float) -> int | float:
    return a * b

# calculator - выводится когда запускаю lessons.py, он в свою очередь импортирует calc и доходит до сюда
# когда запускаю отсюда, выводится __main__
print(__name__)
if __name__ == "__main__":  # проверка означает, что я запускаю именно этот модуль, а не другой. Нужно когда мне
    # нужно запустить именно этот, для юнит-тестов/демо, а не как модуль к-й я импортирую
    # check addition:
    print(add(10, 20))

    # check multiplication:
    print(multiply(10, 20))