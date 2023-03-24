def find_needed_guards(islands: list) -> int:
    f_c = islands.count(False)
    t_c = islands.count(True)
    res = 0 if t_c * 2 >= f_c else f_c // 2
    return res


print(find_needed_guards(([False, False, True, False, True, False, False, False, False])))
