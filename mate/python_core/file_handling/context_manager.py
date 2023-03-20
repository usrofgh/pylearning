# CM always contains 2 methods __enter__ and __exit__
# __enter__ returns an object after as keyboard. Default value None
# if error in __enter__/__exit__, the code block is never executed  and __exit__ is not called. After entering in a
# block __exit__ always will be executed

class CustomContextManager:
    def __init__(self):
        print("init method called")

    def __enter__(self):  # before main body in CM
        print("enter method call")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):  # after main block in CM
        print("exit method called")

    def __del__(self):
        print("with statement block")


with CustomContextManager() as manager:
    # 1 // 0
    print("with statement block")
    # 1 // 0

    # init method called
    # enter method call
    # with statement block
    # exit method called  - will be run in any way, with any mistake in CM body
    # with statement block


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None  # Добавим потом в __etner__

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager("text.txt", "w") as file:
    file.write("test")


# instead of creating own context manager like FileManager you can use:
from contextlib import contextmanager


@contextmanager
def open_file(name, method):
    f = open(name, method)
    try:
        yield f  # она пойдет в переменную после as
    finally:
        f.close()


with open_file("text.txt", "r") as file:
    print(file.read())  # test