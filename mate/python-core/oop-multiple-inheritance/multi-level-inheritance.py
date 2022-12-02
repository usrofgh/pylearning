class User:  # Можно только получить и-ю о юзере
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name} (age: {self.age})")


class Staff(User):  # Один уровень наследования. Может входить в Админ панель
    def __init__(self, name: str, age: int):
        super(Staff, self).__init__(name, age)
        self.is_staff = True

    def login_to_admin_panel(self):
        print(f"{self.name} is entering Admin panel!")


class Moderator(Staff):   #
    def __init__(self, name: str, age: int):
        super(Moderator, self).__init__(name, age)
        self.is_admin = False

    def change_article(self):  # Не просто сотрудник, а модератор,
        # кроме входа в админ-панель и её чтения может изменить  какое-либо значение там
        print(f"{self.name} changed Article!")
        print(self.is_staff)


class Admin(Staff):  # Кроме модераторов сотрудники бывают и админами
    def __init__(self, name: str, age: int):
        super(Admin, self).__init__(name, age)
        self.is_admin = False

    def create_new_staff(self):  # Не занимаются что меняют статьи как в Moderator,
        # но могут создавать новых сотрудников
        print(f"{self.name} created new Staff!")


john = Staff("John", 25)
john.print_info()  # User's method
john.login_to_admin_panel()  # Staff's method

petia = Moderator("Petia", 30)
petia.print_info()
petia.login_to_admin_panel()
petia.change_article()
# petia.change_article() ошибка, так как не наследовались от Admin

ivan = Admin("Ivan", 27)

ivan.print_info()
ivan.login_to_admin_panel()
ivan.create_new_staff()
# ivan.change_article()  # Ошибка если наследуемся от Staff. нет ошибки если от Moderator