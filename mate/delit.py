from __future__ import annotations
from typing import Union


class LowerPrime:
    def __init__(self, number: int) -> None:
        self.number = number
        self.current_number = number

    def __iter__(self) -> LowerPrime:
        self.current_number = self.number
        return self

    def __next__(self) -> Union[int, StopIteration]:
        for num in range(self.current_number - 1, 1, -1):
            if self.is_prime(num):
                self.current_number = num
                return num
        raise StopIteration

    @staticmethod
    def is_prime(number: int) -> bool:
        for divisor in range(2, number // 2 + 1):
            if number % divisor == 0:
                return False
        return True

l = iter(LowerPrime(10))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
