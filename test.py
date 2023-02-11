class GrandFather:
    @staticmethod
    def drink():
        print("I'm drinking")


class Father(GrandFather):
    pass


class Mother:
    @staticmethod
    def cooking():
        print("I'm cooking")

    @staticmethod
    def go_work():
        print("I'm going to salon")


class Son(Father, Mother):
    @staticmethod
    def go_school():
        print("I'm going to school")


son = Son()
son.drink()
# son.go_fishing()
son.cooking()
son.go_work()
print(Son.mro())
