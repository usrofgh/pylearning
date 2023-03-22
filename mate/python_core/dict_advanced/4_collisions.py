# что если 2 объекта имеют одинаковый хеш?


# https://prnt.sc/H9JfYDVnLDW3 - тут колиззия
# r1, r2 имели одинаковый хеш, но разные экз. класса(разные ячейки)
# r3, r4 имели одинаковый хеш и были равны друг другу
# 14 % 8 дал тот же результат что и 30 % 8, поэтому ссылалось на одну и ту же ячейку памяти, и по скольку еще были
# одинаковые объекты, то произошла перезапись вместо дозаписи, если бы объекты были разными, то дописалось бы значение
# вниз как с r1, r2


# для избежания коллизий python юзает открытую адресацию
# Если бы python нужно было записать значению в уже заполненую ячейку, он бы не создавал цепь записей, а просто занял
# следующую пустую ячейку. https://prnt.sc/--WkUiOjtoSt - тут r2 в 7, r3 в 0, r4 перезапись в 7, так как одинаковые
# объекты. Но по факту python рандомит переход в следующую пустую ячейку


# почему коллизии плохо? - они меняют работу с O(1) до O(n), так как приходится из-за коллизий ходить по другим
# ячейкам памяти в зависимости от количества этих коллизий
# в Случае hash в python в среднем его работа O(1)

# если hash table заполнена больше на 2/3 то ее размер увеличится в 2 раза. В этот момент прохожусь по значениям
# подсчета ячейки для записи, и пересчитать, так как теперь не % 8 а % %n. Происходит перезапись, вероятность коллизий
# уменьшается