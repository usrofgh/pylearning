class Grow:
    def __init__(self, stem_diff: float = 0.0, leaf_diff: float = 0.0):
        self.stem_diff = stem_diff
        self.leaf_diff = leaf_diff

    def add(self, other):
        return Grow(
            stem_diff=self.stem_diff + other.stem_diff,
            leaf_diff=self.leaf_diff + other.leaf_diff,
        )


day1 = Grow(stem_diff=2.5)
day2 = Grow(stem_diff=2.0)
day3 = Grow(stem_diff=1.0, leaf_diff=1.5)
day4 = Grow(stem_diff=0.8, leaf_diff=1.2)

plant = day1.add(day2).add(day3).add(day4)  # хотелось бы просто прибавить плюсами, для этого нужны магические методы
print(plant.stem_diff)  # 6.3
print(plant.leaf_diff)  # 2.7

#----------------------------------------------------------------------------------------------------------------------
# в магических методах нужно по 2 нижних подчеркивания
# init - магический
# dir(10) - показывает все методы аттрибута класса(в том числе и магически)
# При создании экземпляра класса сначала вызывается __new__, только потом __init__


class GrowMagic:
    def __init__(self, stem_diff: float = 0.0, leaf_diff: float = 0.0):
        self.stem_diff = stem_diff
        self.leaf_diff = leaf_diff

    def __add__(self, other):
        if not isinstance(other, GrowMagic):
            raise TypeError(f"unsupported operand type(s) for +: 'Grow' and {type(other)}'")
        return GrowMagic(
            stem_diff=self.stem_diff + other.stem_diff,
            leaf_diff=self.leaf_diff + other.leaf_diff,
        )

    # __str__ для чтения, repr - больше для программного использования. Оба возвращают объект преобразованный в строку

    # По умолчанию, если не указывать реализацию __str__, то неявно сделается таким:
    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"Grow(stem_diff={self.stem_diff}, leaf_diff={self.leaf_diff})"


day1 = GrowMagic(stem_diff=2.5)
day2 = GrowMagic(stem_diff=2.0)
day3 = GrowMagic(stem_diff=1.0, leaf_diff=1.5)
day4 = GrowMagic(stem_diff=0.8, leaf_diff=1.2)

# магический метод __add__ понимает, что там где +, нужно использовать __add__
plant = day1 + day2 + day3 + day4
print(plant.stem_diff)  # 6.3
print(plant.leaf_diff)  # 2.7
# day1 + 4  # TypeError: unsupported operand type(s) for +: 'Grow' and <class 'int'>'

# Без реализации __repr__:
# print(plant)  # <__main__.GrowMagic object at 0x000001E8A6C5FDC0>
# print(str(plant))  # <__main__.GrowMagic object at 0x000001E8A6C5FDC0>

# С реализацией __repr__:
print(plant)  # Grow(stem_diff=6.3, leaf_diff=2.7) - __repr__
print(str(plant))  # Grow(stem_diff=6.3, leaf_diff=2.7) - __str__


print(dir(GrowMagic), end=' ')  # выводит магические методы
# ['__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__']