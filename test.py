from __future__ import annotations

class NumberInfo:
    def __init__(self, number: int | float) -> None:
        self._number = number

    @property
    def number(self) -> int | float:
        return self._number

    @number.setter
    def number(self, new_value: int) -> None:
        self._number = new_value

    @property
    def len_digits(self) -> int:
        return len(str(self._number).split(".")[0])

    @property
    def is_integer(self) -> bool:
        return isinstance(self._number, int)

    @property
    def is_float(self) -> bool:
        return isinstance(self._number, float)

    @property
    def decimal(self) -> int:
        if self._number % 1 != 0:
            return len(str(self._number).split(".")[-1])
        return 0

    @property
    def is_positive(self) -> bool:
        return self._number > 0

    @property
    def is_natural(self) -> bool:
        return self._number % 1 == 0 and self._number > 0

    @property
    def is_prime(self) -> bool:
        if isinstance(self._number, float) or self._number < 2:
            return False

        for i in range(2, self._number):
            if (self._number % i) == 0:
                return False
        return True


number_int = NumberInfo(False)

print(number_int.number)
print(number_int.len_digits)
print(number_int.is_integer)
print(number_int.is_float)
print(number_int.decimal)
print(number_int.is_positive)
print(number_int.is_natural)
print(number_int.is_prime)
print("-----------------------------")
