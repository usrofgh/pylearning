class User:
    role = "user"

    def __init__(self, name: str):
        self.name = name

    def print_info(self):
        print(f"Name: {self.name}")


class Admin(User):
    role = "admin"  # перезаписываем

    def __init__(self, name: str, surname: str):  # если родительский конструктор не подходит, то перезаписываем его
        # super - зарезервировано за родительским классом.
        super().__init__(name)  # При инициализации Admin я сначала выполняю родительский конструктор, а потом уже то,
        # что тут
        self.surname = surname

    def auth(self):
        print(f"Admin {self.name} authorized")
    
    def print_info(self):
        # super(Admin, self).print_info()  # берем родительский метод у класса Admin для объекта self и вызвать метод
        # Более короткий вариант
        super().print_info()
        # Потом дописываем что нужно тут    
        print(f"Surname {self.surname}")

dania = User("user")
yaroslav = Admin("yaroslav", "smith")

print(dania.__dict__)  # {'name': 'user'}
print(yaroslav.__dict__)  # {'name': 'yaroslav', 'surname': 'smith'}
yaroslav.print_info()  # Name: yaroslav  Surname smith