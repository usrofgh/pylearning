# В generators не нужно создавать классы, в них методы, достаточно просто создать функцию
# Решается проблема памяти при чтении больших датасетов/данных


def add_substract_multiply_divide(num: int):
    start = 10

    after_addition = start + num
    yield after_addition

    after_subtraction = after_addition - num
    yield after_subtraction

    after_multiplication = after_subtraction * num
    yield after_multiplication

    after_division = after_multiplication / num
    yield after_division


operations_with_5 = add_substract_multiply_divide(5)
print(next(operations_with_5))  # 15
print(next(operations_with_5))  # 10
print(next(operations_with_5))  # 50
print(next(operations_with_5))  # 10.0
# print(next(operations_with_5)) # StopIteration error
# Чтобы итерироватьяс по новой, нужно повторно вызвать функцию
print(next(add_substract_multiply_divide(1)))  # 11

for item in add_substract_multiply_divide(1):
    print(item)  # 11  10 10 10.0

numbers = [1, 2, 3, 4, 5]
print([num ** 2 for num in numbers])  # [1, 4, 9, 16, 25] // Это генератор, ниже  тоже самое:
generator = (num ** 2 for num in numbers)
print(next(generator))  # 1
print(next(generator))  # 4
print(next(generator))  # 9
print(next(generator))  # 16
print(next(generator))  # 25# В generators не нужно создавать классы, в них методы, достаточно просто создать функцию


def add_substract_multiply_divide(num: int):
    start = 10

    after_addition = start + num
    yield after_addition

    after_subtraction = after_addition - num
    yield after_subtraction

    after_multiplication = after_subtraction * num
    yield after_multiplication

    after_division = after_multiplication / num
    yield after_division


operations_with_5 = add_substract_multiply_divide(5)
print(next(operations_with_5))  # 15
print(next(operations_with_5))  # 10
print(next(operations_with_5))  # 50
print(next(operations_with_5))  # 10.0
# print(next(operations_with_5)) # StopIteration error
# Чтобы итерироватьяс по новой, нужно повторно вызвать функцию
print(next(add_substract_multiply_divide(1)))  # 11

for item in add_substract_multiply_divide(1):
    print(item)  # 11  10 10 10.0

numbers = [1, 2, 3, 4, 5]
print([num ** 2 for num in numbers])  # [1, 4, 9, 16, 25] // Это генератор, ниже  тоже самое:
generator = (num ** 2 for num in numbers)
print(next(generator))  # 1
print(next(generator))  # 4
print(next(generator))  # 9
print(next(generator))  # 16
print(next(generator))  # 25

print(sum([i ** 2 for i in numbers]))  # 55
# То же самое можно сделать не для списка, а для генератора:
print(sum(i ** 2 for i in numbers))  # 55
# Разница есть. В 1-м сначала нужно создать новый список, и только потом сделать сумму.
# Во 2-м сразу делаем сумму проходясь по генератору. 2-й вариант быстрее

print(sum([i ** 2 for i in numbers]))  # 55
# То же самое можно сделать не для списка, а для генератора:
print(sum(i ** 2 for i in numbers))  # 55