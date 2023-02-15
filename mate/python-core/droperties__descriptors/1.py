# Descriptors
# Rewrite it to use descriptor

class Age:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if instance.age < 18:
            raise ValueError("Age of adult must be >= 18")
        self._age = value


class Adult:
    age = Age()

    def __init__(self, age: int):
        self.age = age

    def celebrate_birthday(self):
        self.age += 1


adult = Adult(20)
adult.celebrate_birthday()
adult.age


