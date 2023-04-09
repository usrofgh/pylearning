from itertools import permutations


def max_redigit(num: int) -> int:
    if num < 1 or len(str(num)) != 3:
        return None
    return int(max(["".join(el) for el in list(permutations(str(num)))]))
