from abc import ABC, abstractmethod


class A(ABC):

    # @abstractmethod
    # def test(self):
    #     print('a')

    def test1(self):
        pass

    @property
    def f(self):
        return "parent_class"


class B(A):
    pass


a = A()
b = B()
a.test1()
b.test1()