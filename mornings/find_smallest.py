def find_smallest(lst: list, number: int) -> list:
    sorted_list = sorted(list(enumerate(lst)), key=lambda x: x[1])[:number]
    return [x[1] for x in sorted(sorted_list)]


print(find_smallest([1, 2, 3, -4, 0], 3))
