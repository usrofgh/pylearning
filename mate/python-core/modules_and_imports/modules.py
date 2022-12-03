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
sleep(0.5)  # Вызвалась импортированная функция, а не моя, если бы поставили перед своей - вызвалась бы своя
# Импортируется 28 лишних функций
print(len((dir(time))))

print(time.__name__)  # time // получить имя модуля указанной функции


# В консоле:
# python main.py - запускаю все что есть в файле
# python -m main - запускаю конкретный модуль

# Когда запускаем из консоли python app/run.py выдает ошибку.
#  Так как файл сам по себе, он не видит родительский пакет/папку. Поэтому выдаст ошибку импорта,
# Чтобы избежать, нужно запускать как модуль, а не как файл - python -m app.run
# Чтобы pycharm понимал, есть модуль app, а в нем модуль run

# Порядок импорта:
# 1. Standard library imports:
import os
import math
from time import time  # сначала import, потом from

# 2. Third party imports(к-е скачиваем с инета):
# import jupyter
# import requests
# from requests import get

# 3. local application specific imports(к-е написал я):
from packages import calculator
