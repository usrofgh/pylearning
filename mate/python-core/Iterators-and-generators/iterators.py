# from __future__ import annotations
#
#
# class LowerPrime:
#     def __init__(self, number: int) -> None:
#         self.number = number
#
#     def __iter__(self) -> LowerPrime:
#         self.index = self.number - 1
#         return self
#
#     def __next__(self) -> int:
#         if self.index == 1:
#             raise StopIteration
#
#         for i in range(self.index, 1, -1):
#             p = (2**i-1) % i
#             if p == 1:
#                 self.index = i - 1
#                 return i
#
#
# iter_object = iter(LowerPrime(999))
# for i in range(168):
#     print(next(iter_object))


# def time_range(time_start: tuple, time_end: tuple) -> tuple:
#     sec_start = (time_start[0] * 60 * 60) + (time_start[1] * 60) + time_start[2]
#     sec_end = (time_end[0] * 60 * 60) + (time_end[1] * 60) + time_end[2]
#     times = abs(sec_end - sec_start)
#
#     for i in range(times):
#         curr_sec = sec_start + i
#         hours = curr_sec // 3600
#         minutes = (curr_sec % 3600) // 60
#         seconds = (curr_sec % 3600) % 60
#
#         yield hours, minutes, seconds
#
#
# t_range = time_range(time_start=(23, 59, 59),
#                      time_end=(0, 0, 2))
# print(next(t_range))
# print(next(t_range))
# print(next(t_range))

def buy_and_sell_stock(prices: list) -> int:
    profits = []
    for i in range(len(prices)):
        buy_day_price = max(prices[i::])
        if buy_day_price > prices[i]:
            profit = buy_day_price - prices[i]
            profits.append(profit)

    return max(profits) if profits else 0


print(buy_and_sell_stock([10000000000000000, 0]))


class PowTwoInfinite:
    def __iter__(self):
        self.current_power = 0
        return self

    def __next__(self):
        result = 2 ** self.current_power
        self.current_power += 1
        return result

# тут неявно вызывается inter()
list(PowTwoInfinite())