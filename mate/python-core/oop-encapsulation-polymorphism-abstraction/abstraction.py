# Abstraction не все включают в ООП.
# Abstraction is the OOP concept that shows only essential attributes and hides unnecessary information.
# The main purpose of abstraction is to hide unnecessary details from the users.
# Abstraction selects data from a larger pool to show only relevant details of the object to the user.
# It helps in reducing programming complexity and efforts

# Кафе имеет имя, публичные методы открытия, заказа кофе, остальные методы спрятаны от посетителя
class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
        self._workers = ["John", "Kate", "Bob"]

    @staticmethod
    def open():
        print("Cafe is working!")

    def order_coffee(self):
        if len(self._workers) > 0:
            print("Making coffee...")
            print("Please, here you are!")
        else:
            print("Error")

    def _sick_leave(self, worker: str):
        self._workers.remove(worker)

    def _skip_job(self, worker: str):
        self._workers.remove(worker)

    def _ask_overtime(self, different_worker: str):
        self._workers.append(different_worker)

best_cafe = Cafe("The Best Ever Coffee")

# Хотелось бы, чтобы все работало как ниже, без проблем, но сотрудники могут увольняться/болеть
# как следствие, процесс открытия меняется
best_cafe.open()
best_cafe.order_coffee()
#--------------------------------------------------------------------------------------------


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
        self._workers = ["John", "Kate", "Bob"]

    def open(self):
        print("Cafe is working!")
        self._sick_leave("John")  # уволился
        self._sick_leave("Kate")  # заболел
        self._skip_job("Bob")  # просто пропустил работу

        self._ask_overtime("Jane")

    def order_coffee(self):
        if len(self._workers) > 0:
            print("Making coffee...")
            print("Please, here you are!")
        else:
            print("Error")

    def _sick_leave(self, worker: str):
        self._workers.remove(worker)

    def _skip_job(self, worker: str):
        self._workers.remove(worker)

    def _ask_overtime(self, different_worker: str):
        self._workers.append(different_worker)

best_cafe = Cafe("The Best Ever Coffee")
best_cafe.open()  # Cafe is working
best_cafe.order_coffee()  # Error. Звоним другому человеку в функции open
# Для посетителя существует только open/order_coffee. В зависимости от разных ситуаций
# внутри реализации этих открытых функций могут выполняться protected(скрытые вне класса)


# В этом примере со стороны начальника абстракции нет, начальник живет полностью внутренней жизнью класса Cafe
# Что я могу сделать как клиент:
print(best_cafe.name)  # посмотреть имя кафе
best_cafe.order_coffee()  # как для посетителя мне не важно что какой-то сотрудник заболел/уволился, вышел на смену
# От всех этих деталей я абстрагирован и просто вижу, что когда я заказал кофе - я его получаю 
