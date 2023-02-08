def fibonacci_generator(number: int) -> None:
    a, b = 0, 1

    for _ in range(number):
        yield a
        a, b = b, a + b

f = fibonacci_generator(6)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))