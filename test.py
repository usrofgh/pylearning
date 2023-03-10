def performant_smallest(nums: list, n: int) -> list:
    values = sorted(enumerate(nums), key=lambda x: x[1])[:n]
    print(type(values[0]))
    return [i[1] for i in sorted(values)]
print(performant_smallest([1, 2, 4, 1, 2], 3))
