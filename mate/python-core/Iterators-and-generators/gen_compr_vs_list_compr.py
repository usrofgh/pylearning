# Разница в требовании памяти генератор vs лист
# Генератор всегда юзает фиксированное к-во памяти. Лист - в зависимости от размера данных

import sys
import cProfile
n = 50_000_000
n_lc = [i ** 2 for i in range(n)]
r1 = sys.getsizeof(n_lc)

n_gc = (i ** 2 for i in range(n))
r2 = sys.getsizeof(n_gc)

# test with 50_000_000
print(f"List comprehension needs memory: {r1}")  # 411943896
print(f"Generator comprehension needs memory: {r2}")  # 208
print(f"Generator comprehension needs less in {round(r1 / r2)} times")  # 3960999


#Если нет перегрузки памяти - быстрее list comprehension, так как gen юзает только фикс. к-во ячеек памяти, лист больше.
# Если есть перегрузка, быстрее gen compr. Так как
# у list происходит перегрузка памяти, а gen продолжает работать

cProfile.run('sum([i * 2 for i in range(n)])')  # 5 function calls 3.859 seconds
cProfile.run('sum((i * 2 for i in range(n)))')  # 5000005 function calls in 9.567 seconds
