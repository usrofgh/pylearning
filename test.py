def generate_rows(rows: int) -> list:
    numbers = [1]

    for k in range(1, rows):
        numbers.append(numbers[-1] * (rows - k) // k)

    print(numbers)

print(generate_rows(5))
