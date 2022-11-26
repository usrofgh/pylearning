# Cat/Dog - дочерние классы
# Animal - Родительский

class Animal:
    def eat(self):
        print("I am eating")

    def sleep(self):
        print("💤💤💤")


class Cat(Animal):
    pass


class Dog(Animal):
    def bark(self):
        print("I am barking")

cat = Cat()
dog = Dog()

cat.eat()
cat.sleep()

dog.eat()
dog.bark()
#-----------------------------------------------------------------------------------------------------------------------
# Example:


class User:
    role = "user"

    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name} is {self.age}")


class Admin(User):
    role = "admin"  # перезаписываем

    def auth(self):
        print(f"Admin {self.name} authorized")

user = User("user")
admin = Admin("admin", 42)
admin.print_info()
