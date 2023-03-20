# from https://mate.academy/learn/python-core/python-core-properties-and-descriptors#/practice/python_school_diary

class Grade:
    def __init__(self) -> None:
        self.minvalue = 2
        self.maxvalue = 12

    def __set_name__(self, owner, name) -> None:
        self.public_name = name
        self.protected_name = "_" + name

    def __get__(self, instance, owner) -> int:
        return getattr(instance, self.protected_name)

    def __set__(self, instance, value) -> None:
        if not isinstance(value, int):
            raise TypeError("Grade should be integer")
        if value < 2 or value > 12:
            raise ValueError(f"Grade should not be less than {self.minvalue} and greater than {self.maxvalue}")

        setattr(instance, self.protected_name, value)


class SchoolDiary:
    math = Grade()
    history = Grade()
    literature = Grade()

    def __init__(self, math: int, history: int, literature: int) -> None:
        self.math = math
        self.history = history
        self.literature = literature
