from functools import wraps


def delay(seconds: int) -> callable:
    """
    delay function
    """
    def inner(func: callable):
        """
        inner function
        """
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            """
            wrapper function
            """
            import time
            s = time.perf_counter()
            time.sleep(seconds)
            func(*args, **kwargs)
            e = time.perf_counter()
            print('Elapsed: ', e - s)
        return wrapper
    return inner


@delay(seconds=3)
def hello_name(msg: str) -> None:
    """
    hello name function
    """
    print(f"Hello, {msg}!")


hello_name("Nikita")

