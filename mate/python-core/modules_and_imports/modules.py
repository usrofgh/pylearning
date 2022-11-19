# встроенный модуль(python файл), содержащий какие-то переменные/константы, функции
import time
# н-е функции в модуле возвращают return "" - на самом деле реализация просто спрятана
# многие функции реализованы на языке C

# import random, math  # bad practice
#--------- Good ------
import random
import math
#---------------------

import time as s  # alias
from time import time  # import function from module
from time import time, sleep  # good practice


def sleep(hourse: int):
    print(f"Go to the bad for {hourse} hours")
# Bad practice. Может произойти коллизия с другими функциями
from time import *
sleep(0.5)  # Вызвалась импортированная функция, а не моя
# Импортируется 28 лишних функций
print(len((dir(time))))

print(time.__name__)  # time // получить имя модуля указанной функции