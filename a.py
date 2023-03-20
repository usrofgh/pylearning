def shortest_step(goal_num: int) -> int:
    n = goal_num
    i = 0
    while True:
        if n == 1:
            return i
        if n % 2 == 0:
            n = n / 2
        else:
            n = n - 1
        i += 1


print(shortest_step(78  ))
