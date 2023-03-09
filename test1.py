def sum_of_a_sequence(begin_number: int, end_number: int, step: int) -> int:
    return 0 if begin_number > end_number else sum(range(begin_number, end_number + 1, step))

print(sum_of_a_sequence(begin_number = 2, end_number = 2, step = 1))