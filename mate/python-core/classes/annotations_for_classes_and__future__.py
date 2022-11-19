from __future__ import annotations  # нужно чтобы в py 3.10 можно было указать аннотацию Age, иначе будет ошибка
# исправлена в 3.11


class Age:
    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: Age | int) -> Age:  # Если версия <3.10, то юзать Union(Age, int)
        if isinstance(other, Age):
            return Age(self.value + other.value)

        return Age(self.value + other)

    def __str__(self) -> str:
        return f"Age: {self.value}"


if __name__ == "__main__":
    print(Age(25) + Age(13))
    print(Age(25) + 10)
    # print(Age(25) + "10") # TypeError: unsupported operand type(s) for +: 'int' and 'str'