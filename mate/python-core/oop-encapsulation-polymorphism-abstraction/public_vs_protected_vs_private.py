class Base:
    def __init__(self):
        self.zero = "public "  # outside class/child, outside
        self._first = "protected "  # inside class/child
        self.__second = "private "  # inside class

    def public_method(self):
        return self.zero + self._first + self.__second

    @staticmethod
    def _protected():
        return "call_protected"

    @staticmethod
    def __private():
        return "call_private"


class ChildBase(Base):
    pass

base = Base()
child_base = ChildBase()

# Good practice run public methods outside a class
print(base.public_method())  # public protected private
print(child_base.public_method())  # public protected private

# Bad practice use protected attributes/methods outside a class
base._first = "new protected"
print(base._protected())  # call_protected
print(child_base._protected())  # call_protected


# print(base.__private())  # object has no attribute '__private
# print(child_base.__private())  # object has no attribute '
print(base._Base__private())  # call_private
# print(child_base._ChildBase__private())  # 'ChildBase' object has no attribute '_ChildBase__private'


# bad practice
# base.__second  # error
base._Base__second = "new private"
print(base._Base__second)  # new private
print(base._Base__private())  # call_private


class Derived(Base):
    def __init__(self):
        super().__init__()

        # ok practice. Derived is a child class
        print("Protected member of Base class:", self._first)
        self._protected()

        # bad practice. We try to get a private attribute
        print("Private member of Base class:", self.__second)
        self.__private()

# base._protected() - we don't get suggestions.
# base.public_method() - we get suggestion
# Encapsulation hide unnecessary functionality from a programmer
