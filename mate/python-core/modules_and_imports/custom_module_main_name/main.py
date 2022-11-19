import calculator

# Когда мы что-то импортируем из модуля - он полностью выполняется
# Вместо 3-х print'ов ниже также выполнятся принты в самом модуле, к-е созданы для тестирования функций
# Чтобы этого избежать обверни тестируемые функции в модуле в "if __name__ == "__main__":"


from calculator import multiply

print(__name__)  # __main__
print(calculator.CALCULATOR_VERSION)
print(calculator.add(2, 4))
print(multiply(2, 4))


