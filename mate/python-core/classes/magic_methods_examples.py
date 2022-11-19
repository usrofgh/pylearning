# Комплексное число состоит из двух частей:
# c = a + bi
#   a - действительная часть
#   bi - мнимая часть:
#       b - действительное число.
#       i - специальное число. К-е в квадрате дает -1
#           i ** 2 = -1

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(
            real=self.real + other.real,
            imag=self.imag + other.imag
        )

    def __sub__(self, other):
        return Complex(
            real=self.real - other.real,
            imag=self.imag - other.imag
        )

    def __mul__(self, other):
        return Complex(
            # ac - bd
            real=self.real * other.real - self.imag * other.imag,
            # bc + ad
            imag=self.imag * other.real + self.real * other.imag
        )

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    # __str__ для чтения, repr - больше для программного использования. Оба возвращают объект преобразованный в строку
    # Если не реализовывать str он просто будет возвращать repr(self)
    def __repr__(self):
        return f"Complex(real={self.real}, imag={self.imag})"

    def __str__(self):
        return f"{self.real} + {self.imag}i"


first = Complex(1, 2)
second = Complex(-2, 3)
third = Complex(1, 2)
print(repr(first + second))  # Complex(real=-1, imag=5)
print(first + second)  # -1 + 5i

print(repr(first - second))  # Complex(real=3, imag=-1)
print(first - second)

print(repr(first * second))  # Complex(real=-8, imag=-1)

a = 5
print(first + a)  # 6 + 2i // Ошибки НЕ произошло, так как 5 тоже объект, и у него также есть аттрибут imag, real
print(a.real, a.imag)  # 5 0 // у 5 есть настоящая и мнимая часть(0)
# Комплексные числа УЖЕ встроены в python, поэтому first + a отработал
# Если бы я назвал аттрибуты НЕ real/imag а по другому - ничего бы не сработало

print(first == third)  # True
