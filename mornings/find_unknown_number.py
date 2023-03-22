def find_unknown_number(first: int, second: int, third: int) -> int:
    i = 1
    while True:
        f = i % 3 == first
        s = i % 5 == second
        t = i % 7 == third
        if all([f, s, t]):
            return i
        i += 1


print(find_unknown_number(1, 1, 1))
