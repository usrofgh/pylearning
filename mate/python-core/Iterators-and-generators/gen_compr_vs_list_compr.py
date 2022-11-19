# Разница в требовании памяти генератор vs лист
# Генератор всегда юзает фиксированное к-во памяти - 208. Лист - в зависимости от размера данных

import sys
import cProfile
n_lc = [i ** 2 for i in range(5000000)]
r1 = sys.getsizeof(n_lc)

n_gc = (i ** 2 for i in range(5000000))
r2 = sys.getsizeof(n_gc)

print(f"List comprehension needs memory: {r1}")  # 43947864
print(f"Generator comprehension needs memory: {r2}")  # 208
print(f"Generator comprehension needs less in {round(r1 / r2)} times")  # 211288


# Если нет перегузки памяти - быстрее list compregension, так как gen юзает только 208 ячеек памяти, лист больше. Если есть перегрузка, быстрее gen compr. Так как
# у list происходит перегрузка памяти, а gen продолжает работать

cProfile.run('sum([i * 2 for i in range(5000000)])')  # 5 function calls in 1.135 seconds
cProfile.run('sum((i * 2 for i in range(5000000)))')  # 5000005 function calls in 3.630 seconds
