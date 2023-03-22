#
#
# def pascal_triangle_row(row_index: int) -> list:
#     prev = 1
#     res = [1]
#     for i in range(1, row_index + 1):
#         curr = (prev * (row_index - i + 1)) // i
#         res.append(curr)
#         prev = curr
#     return res
#
#
# print(pascal_triangle_row(3))

def zero(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(0) + plus_res)
    return 0


def one(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(1) + plus_res)
    return 1


def two(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(2) + plus_res)
    return 2


def three(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(3) + plus_res)
    return 3


def four(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(4) + plus_res)
    return 4


def five(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(5) + plus_res)
    return 5


def six(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(6) + plus_res)
    return 6


def seven(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(7) + plus_res)
    return 7


def eight(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(8) + plus_res)
    return 8


def nine(plus_res: str = None) -> int:
    if plus_res:
        return eval(str(9) + plus_res)
    return 9


def plus(n: int) -> str:
    return f" + {str(n)}"


def minus(n: int) -> str:
    return f" - {str(n)}"


def times(n: int) -> str:
    return f" * {str(n)}"


def divided_by(n: int) -> str:
    return f" // {str(n)}"


print(
    zero(times(one())),
)