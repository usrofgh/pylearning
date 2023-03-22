from typing import Callable, Union


def zero(func: Callable = None) -> Union[Callable, int]:
    return 0 if not func else func(0)


def one(func: Callable = None) -> Union[Callable, int]:
    return 1 if not func else func(1)


def two(func: Callable = None) -> Union[Callable, int]:
    return 2 if not func else func(2)


def three(func: Callable = None) -> Union[Callable, int]:
    return 3 if not func else func(3)


def four(func: Callable = None) -> Union[Callable, int]:
    return 4 if not func else func(4)


def five(func: Callable = None) -> Union[Callable, int]:
    return 5 if not func else func(5)


def six(func: Callable = None) -> Union[Callable, int]:
    return 6 if not func else func(6)


def seven(func: Callable = None) -> Union[Callable, int]:
    return 7 if not func else func(7)


def eight(func: Callable = None) -> Union[Callable, int]:
    return 8 if not func else func(8)


def nine(func: Callable = None) -> Union[Callable, int]:
    return 9 if not func else func(9)


def plus(input_number: int) -> int:
    return lambda number: number + input_number


def minus(input_number: int) -> int:
    return lambda number: number - input_number


def times(input_number: int) -> int:
    return lambda number: number * input_number


def divided_by(input_number: int) -> int:
    return lambda number: number // input_number