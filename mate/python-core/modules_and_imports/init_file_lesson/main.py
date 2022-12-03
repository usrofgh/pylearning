# import pkg  # I'm in __init__
# import pkg  # Ничего не выведет. 2-й раз пакет инициализирован не будет
import pkg.mod1  # I'm in __init__      I'm in mod1.py
from pkg.mod2 import func1  # I'm in __init__    I'm in mod1.py