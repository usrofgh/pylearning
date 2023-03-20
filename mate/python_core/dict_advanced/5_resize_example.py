import sys


my_dict = {}
prev = sys.getsizeof(my_dict)

print(f"0. bit = {prev}. byte = {prev // 8}")
for i in range(1000):
    my_dict[i] = ""
    s = sys.getsizeof(my_dict)
    if prev != s:
        prev = s
        print(f"{i+1}. bit = {s}. byte = {prev //  8}")

# 0. bit = 64. byte = 8
# 1. bit = 224. byte = 28
# 6. bit = 352. byte = 44
# 11. bit = 632. byte = 79
# 22. bit = 1168. byte = 146
# 43. bit = 2264. byte = 283
# 86. bit = 4688. byte = 586
# 171. bit = 9304. byte = 1163
# 342. bit = 18512. byte = 2314
# 683. bit = 36952. byte = 4619

# пустой dict - 64 бит(8 байт)

# почему расширение было после 5-го, 10-го, 21 э-в?
# int(8) * (2 / 3) = 5 THRESHOLD. При 8 байт, 2/3 - 5. Как только нужно вписать 6-й э-т - увеличиваю в 2 раза
# при 16 байт макс 10 э-в, 11 э-т - будет расширение до 32

# При добавлении 6-го э-та с capacity 8 будет resize, так как мы превысили THRESHOLD значения
# новый словарь с пустыми ячейками, пересчитываем все предыдущие значения hash(key) % capacity = n_cell
# записываем это, и только потом уже записываем новые значения
# https://prnt.sc/ONovUpM7SFLt

# при удалении значений resize dict'а не происходит
d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
print(sys.getsizeof(d) // 8)  # 28
d[6] = 6
print(sys.getsizeof(d) // 8)  # 44
del d[6]
print(sys.getsizeof(d) // 8)  # 44
d.clear()  # now d is {}
print(sys.getsizeof(d) // 8)  # 8

