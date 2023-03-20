CALCULATOR_VERSION = "beta"


def add(a: int | float, b: int | float) -> int | float:
    return a + b


def multiply(a: int | float, b: int | float) -> int | float:
    return a * b


if __name__ == "__main__":
    # check addition:
    print(add(10, 20))

    # check multiplication:
    print(multiply(10, 20))
