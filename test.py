class User:
    def __init__(self, name: str):
        self.name = name


class Moderator(User):
    def login_admin(self):
        print(f"{self.name} log in to Dashboard")


class Admin(Moderator):
    def __init__(self, name: str, surname: str):
        super(Admin, self).__init__(name)
        self.surname = surname


user = User("User")
moderator = Moderator("Moderator")
admin = Admin("Admin", "Admin")

print(User.__dict__)
print(Moderator.__dict__)
print(Admin.__dict__)
