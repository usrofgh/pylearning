class User:
    role = "user"

    def __init__(self, name: str):
        self.name = name

    def print_info(self):
        print(f"Name: {self.name}")


class Admin(User):
    role = "admin"

    def __init__(self, name: str, surname: str):
        super().__init__(name)
        self.surname = surname

    def auth(self):
        print(f"Admin {self.name} authorized")

    def print_info(self):
        super(Admin, self).print_info()
        print(f"Surname {self.surname}")


user = User("Danya")
admin = Admin("Petia", "Smith")
print(isinstance(user, Admin))  # False
print(isinstance(admin, User))  # True (так как наследуется)
print(issubclass(User, Admin))  # False
print(issubclass(Admin, User))  # True

print(type(object))  # type
print(type(type))  # type
print(User.__bases__)  # (<class 'object'>,)
