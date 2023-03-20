from typing import Callable


def tg(tag: str):
    print(f"in tg {tag}")

    def add_tag(func: Callable) -> Callable:
        print("in add_tag")

        def wrapper():
            print("in wrapper")
            func()

        return wrapper
    return add_tag


@tg("div")
@tg("p")
def print_text() -> None:
    print("Hi")


print_text()

