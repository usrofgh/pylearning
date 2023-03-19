def count_nines(number: int) -> int:
    return (number // 10) + (int(str(number)[0]) * 10)


print(count_nines(100))
