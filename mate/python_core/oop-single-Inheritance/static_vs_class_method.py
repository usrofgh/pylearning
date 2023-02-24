# ![](static_vs_class_method.png)
# В ООП лучше юзать classmethod, так как в статике мы возвращаем напрямую Weapon(родительский класс), а не текущий


class Number:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def sum_staticmethod(value1, value2):
        return Number(value1 + value2)

    @classmethod
    def sum_classmethod(cls, value1, value2):
        return cls(value1 + value2)


class Int(Number):
    pass


int_from_staticmethod = Int.sum_staticmethod(1, 2)
print(int_from_staticmethod.__class__)  # <class '__main__.Number'>

int_from_classmethod = Int.sum_classmethod(1, 2)
print(int_from_classmethod.__class__)  # <class '__main__.Int'>