import sys


class Cat:
    def __init__(self, mark: str):
        self.mark = mark


cat = Cat("Cat")
print(sys.getrefcount(cat))  # result 3
pass
pass
pass
print(sys.getrefcount(cat))  # result 7